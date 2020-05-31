from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.home, name='home'),
  path('update/profile/',views.update_profile, name='profileupdate'),
  path('profile/',views.profile, name='profile'),
  path('image/upload/',views.upload_image, name='imageupload'),
  path('single/image/<imageid>',views.single_image,name='singleimage'),
  path('add/comment/<imageid>',views.add_comment,name="addcomment"),
  path('search/profile/',views.search_user,name="profilesearch"),
  path('image/like/<imageid>',views.like_image, name="likeimage"),
  path('follow/user/<userid>',views.follow_user,name="followuser")
]

if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)