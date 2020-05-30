from django import forms
from .models import Profile

class ProfileForm(forms.Form):
  class Meta:
    model = Profile
    exclude = ['user']