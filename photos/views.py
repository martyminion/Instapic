from django.shortcuts import render,redirect
from .models import User,Image,Comments,Profile,Likes
from django.contrib.auth.decorators import login_required
from .form import ProfileForm,ImageForm
from django.http import HttpResponseRedirect
import datetime as dt
# Create your views here.

def home(request):

  title = "Home"
  all_images = Image.objects.all()
  
  context = {"title":title,"all_images":all_images}
  return render(request,'home.html',context)

@login_required
def profile(request):
  title = "Profile"
  current_user = request.user
  userprofile = Profile.get_user_profile(current_user)
  user_images = Image.get_images_by_user(current_user)
  followers = userprofile.followers.all()
  following = userprofile.following.all()
  numfollowers = len(userprofile.followers.all())
  numfollowing = len(userprofile.following.all())
  context = {"title":title,"current_user":current_user,"userprofile":userprofile,"user_images":user_images,"followers":followers,'following':following,
  'numfollowers':numfollowers,'numfollowing':numfollowing}

  return render(request,'profile/profile.html',context)

@login_required
def update_profile(request):
  title = 'Update Profile'
  current_user = request.user
  
  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      photo = form.cleaned_data['profile_photo']
      bio = form.cleaned_data['profile_bio']

      new_profile = Profile.get_user_profile(current_user)
      new_profile.profile_photo = photo
      new_profile.profile_bio = bio

      new_profile.save()
      return redirect(profile)
  else:
    form = ProfileForm()
  context = {"current_user":current_user,"title":title,"form":form}
  return render(request,'profile/profile_update.html',context)

@login_required
def upload_image(request):
  title = 'Image Upload'
  current_user = request.user

  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      new_image = form.save(commit=False)
      new_image.profile = current_user.profile
      new_image.user = current_user
      new_image.upload_date = dt.date.today()
      new_image.save()

    return redirect(profile)
  else:
    form = ImageForm()
  return render(request,'profile/upload_image.html',{"title":title,"form":form})

@login_required
def single_image(request,imageid):
  one_image = Image.get_single_image(imageid)
  title = one_image.image_name
  one_image_comments = Comments.get_comments_image(imageid)
  current_user = request.user

  number_of_likes = Likes.get_number_of_likes(imageid)
  context = {"title":title,"one_image":one_image,"one_image_comments":one_image_comments,"number_of_likes":number_of_likes}
  return render(request,'singleimage.html',context)

@login_required
def add_comment(request,imageid):
  current_user = request.user
  one_image = Image.get_single_image(imageid)

  if 'new_comment' in request.GET and request.GET['new_comment']:
    newcomment = request.GET.get('new_comment')
    user_comment = Comments(comment = newcomment, user = current_user, image = one_image)
    user_comment.save()
  return redirect(single_image, imageid = imageid)
  

  # if request.method == 'POST':
  #   form = CommentForm(request.POST)
  #   if form.is_valid():
  #     new_comment = form.save(commit=False)
  #     new_comment.user = current_user
  #     new_comment.image = one_image
  #     new_comment.save()
  #   return redirect(single_image, imageid = imageid)
  # else:
  #   form = CommentForm()
  # return redirect(single_image, imageid = imageid)

@login_required
def search_user(request):
  title = 'search results'
  if 'searchname' in request.GET and request.GET["searchname"]:
    searchname = request.GET.get("searchname")
    results = Profile.search_user_profile(searchname)
    if len(results)>0:
      return render(request,'results.html',{"title":title,"results":results,"namesearch":searchname})
    else:
      message = "Could not find user with that username"
      return render(request,'results.html',{"title":title,"message":message,"namesearch":searchname})
  else:
    message = "Please enter a valid username"
    return render(request,'results.html',{"title":title,"message":message,"namesearch":searchname})

@login_required
def follow_user(request,userid):
  current_user = request.user
  if userid == current_user.id:
    pass
  else:
    followed_user = Profile.get_user_profile(userid)
    followed_user.followers.add(current_user.profile)
    current_user.profile.following.add(followed_user)
    followed_user.save()
  return redirect(home)


@login_required
def like_image(request,imageid):
  current_user = request.user
  image = Image.objects.get(image_name = imageid)
  likes = Likes.objects.filter(image = image,user = current_user)

  if len(likes)==0:
    Likes.like_an_image(current_user,image)
  else:
    for like in likes:
      if like.like == True:
        like.unlike_an_image()
      elif like.like is False:
        like.relike_an_image()

  return redirect(home)