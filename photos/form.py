from django import forms
from .models import Profile,Image,Comments

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']

class ImageForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude = ['user','profile','likes']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comments
    exclude = ["image","user"]
