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

  userprofile = Profile.get_user_profile(current_user)

  user_images = Image.get_images_by_user(current_user)
  print("X"*30)
  print()
  print("X"*30)
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

