from django.shortcuts import render,redirect
from .models import User,Image,Comments,Profile
from django.contrib.auth.decorators import login_required
from .form import ProfileForm,ImageForm,CommentForm
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):

  title = "Home"
  all_images = Image.objects.all()
  form = CommentForm()

  context = {"title":title,"all_images":all_images,"form":form}
  return render(request,'home.html',context)

@login_required
def profile(request):
  title = "Profile"
  current_user = request.user
  userprofile = Profile.get_user_profile(current_user)
  user_images = Image.get_images_by_user(current_user)

  print('*'*50)
  print(user_images)

  context = {"title":title,"current_user":current_user,"userprofile":userprofile,"user_images":user_images}

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
  form = CommentForm()
  context = {"title":title,"one_image":one_image,"one_image_comments":one_image_comments,"form":form}
  return render(request,'singleimage.html',context)

@login_required
def add_comment(request,imageid):
  current_user = request.user
  one_image = Image.get_single_image(imageid)

  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      new_comment = form.save(commit=False)
      new_comment.user = current_user
      new_comment.image = one_image
      new_comment.save()
    return redirect(single_image, imageid = imageid)
  else:
    form = CommentForm()
  return redirect(single_image, imageid = imageid)

# @login_required
# def follow_user(request,userid):
#   current_user = request.user
#   followed_user = Profile.get_user_profile(userid)
#   followed_user.profile.followers.add(current_user.profile)
#   followed_user.save()

#   return redirect(home)

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
def like_image(request,imageid):
  current_user = request.user
  Likes.like_image(current_user,imageid)
  return HttpResponseRedirect(request.path_info)