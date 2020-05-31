from django.contrib import admin
from .models import Profile,Comments,Image,Likes

# Register your models here.

admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(Image)
admin.site.register(Likes)