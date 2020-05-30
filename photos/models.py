from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Profile(models.Model):
  profile_photo = models.ImageField()
  profile_bio = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  #save a profile
  def save_profile(self):
    self.save()
  
  def update_profile_bio(self,new_bio):
    self.profile_bio = new_bio
    self.save()
  
  def update_profile_photo(self,new_photo):
    self.profile_photo = new_photo
    self.save()
  
  def delete_profile(self):
    self.delete()

  def __str__(self):
    return self.profile_bio



class Comments(models.Model):
  comment = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  @classmethod
  def delete_comment(cls,username,name):
    cls.objects.filter(user = username).filter(image = name).delete()
  
  def __str__(self):
    return self.comment 

class Image(models.Model):
  image = models.ImageField(upload_to = 'photos/' )
  image_name = models.CharField(max_length=50)
  image_caption = models.TextField(blank=True)
  profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
  likes = models.IntegerField(blank=True)
  comments = models.ManyToManyField(Comments,blank=True)
  user = models.ForeignKey(User, on_delete = models.CASCADE)

  @classmethod
  def get_images_by_user(cls,username):
    images = cls.objects.get(user = username)
    return images

  def get_comments(self):
    comments = self.comments
    return comments

  def __str__(self):
    return self.image_name

