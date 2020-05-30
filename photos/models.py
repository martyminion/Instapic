from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
User = get_user_model()

class Profile(models.Model):
  profile_photo = models.ImageField(upload_to = 'photos/' ,blank=True)
  profile_bio = models.TextField(blank=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)



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
  @classmethod
  def get_user_profile(cls,username):
    user_profile = cls.objects.get(user = username)
    return user_profile


  def __str__(self):
    return self.profile_bio

@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



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

