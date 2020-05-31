from django.shortcuts import render,redirect
from .models import User,Image,Comments,Profile
from django.contrib.auth.decorators import login_required
from .form import ProfileForm,ImageForm
# Create your views here.

def home(request):

  title = "Home"
  return render(request,'home.html',{"title":title})

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
