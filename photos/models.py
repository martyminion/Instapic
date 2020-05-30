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




class Comments():
  comment = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ForeignKey(image, on_delete=models.CASCADE)

  @classmethod
  def delete_comment(cls,username,name):
    cls.objects.filter(user.username = username).filter(image.image_name = name).delete()
  

  @classmethod
  def get_comments_by_user(cls,username):
    comments = cls.objects.get(user.username = username)
    return comments
  @classmethod
  def get_comments_by_image(cls,name):
    comments = cls.objects.get(image.image_name = name)
    return comments
  

class Image(models.Model):
  image = models.ImageField()
  image_name = models.CharField(max_length=50)
  image_caption = models.TextField()
  profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
  likes = models.IntegerField()
  comments = models.ManyToManyField(Comments)
  user = models.ForeignKey(User, on_delete = models.CASCADE)
