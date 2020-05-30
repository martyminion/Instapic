from django.shortcuts import render,redirect

# Create your views here.

def home(request):

  title = "Home"
  return render(request,'registration/login.html',{"title":title})
  