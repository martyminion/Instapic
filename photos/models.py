from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField



# Create your models here.
User = get_user_model()

class Profile(models.Model):
  profile_photo = CloudinaryField('image')
  profile_bio = models.TextField(blank=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  followers = models.ManyToManyField('self',related_name='followers',blank = True)
  following = models.ManyToManyField('self',related_name='following',blank = True)

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
  def get_user_profile(cls,userid):
    user_profile = cls.objects.get(user = userid)
    return user_profile

  def search_user_profile(search_term):
    user_profiles = User.objects.filter(username__icontains = search_term)
    return user_profiles

  def __str__(self):
    return self.user.username

@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Image(models.Model):
  image = CloudinaryField('image')
  image_name = models.CharField(max_length=50)
  image_caption = models.TextField(blank=True)
  profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
  user = models.ForeignKey(User, on_delete = models.CASCADE)

  @classmethod
  def get_images_by_user(cls,userid):
    images = cls.objects.filter(user = userid)
    return images
  @classmethod
  def get_single_image(cls,imageid):
    image = cls.objects.get(id = imageid)
    return image


  def __str__(self):
    return self.image_name

class Comments(models.Model):
  comment = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ForeignKey(Image, on_delete=models.CASCADE)

  @classmethod
  def delete_comment(cls,username,name):
    cls.objects.filter(user = username).filter(image = name).delete()

  @classmethod
  def get_comments_image(cls,imageid):
    comments = cls.objects.filter(image = imageid)
    return comments

  
  def __str__(self):
    return self.image.image_name


class Likes(models.Model):
  like = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ForeignKey(Image,on_delete=models.CASCADE)

  @classmethod
  def get_number_of_likes(cls,imageid):
    number = Likes.objects.filter(like = True, image = imageid).count()
    return number
  
  def like_an_image(userid,imageid):
    new_like = Likes(like = True, user = userid, image = imageid)
    new_like.save()

  def unlike_an_image(self):
   self.like = False
   self.save()
  def relike_an_image(self):
   self.like = True
   self.save()

  def __str__(self):
    return self.image.image_name