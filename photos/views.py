from django.shortcuts import render,redirect
from .models import User,Image,Comments,Profile
from django.contrib.auth.decorators import login_required
from .form import ProfileForm
# Create your views here.

def home(request):

  title = "Home"
  return render(request,'home.html',{"title":title})

@login_required
def profile(request):
  title = "Profile"
  current_user = request.user
  userprofile = Profile.get_user_profile(current_user.username)
  user_images = Image.get_images_by_user(current_user.username)
  context = {"user_images":user_images,"title":title,"current_user":current_user,"userprofile":userprofile}

  return render(request,'profile/profile.html',context)

@login_required
def update_profile(request):
  title = 'Update Profile'
  current_user = request.user
  context = {"current_user":current_user,"title":title}
  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      photo = form.cleaned_data['profile_photo']
      bio = form.cleaned_data['profile_bio']

      new_profile = Profile(profile_photo = photo,profile_bio = bio)
      new_profile.save(commit = False)
      new_profile.user = current_user.username
      new_profile.save_profile()
  else:
    form = ProfileForm()
  
  return render(request,'profile/profile_update.html',context)

