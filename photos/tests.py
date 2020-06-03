from django.test import TestCase
from .models import User,Image,Comments,Profile,Likes
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime as dt
# Create your tests here.

class ImageTest(TestCase):

  def setUp(self):
    self.drew = User.objects.create_user(username = 'Andrew', password = 'admindrew12345')
   
    self.new_Image = Image(image_name = "Test1", image_caption = "This test works", profile = self.drew.profile, user = self.drew, upload_date = dt.date.today() )
    self.new_Image.image = SimpleUploadedFile(name='travel5.jpg',content=open('/home/martin/Documents/Moringa-Core/Django/InstaClone/Instapic/media/travel5.jpg','rb').read(),content_type='image/jpeg')
    self.new_comment = Comments(comment = "Amazing", user = self.drew, image = self.new_Image)
    self.new_like = Likes(like=True,user = self.drew, image = self.new_Image)

    self.new_Image.save()
    self.new_comment.save()
    self.new_like.save()

    '''
    Tests
    '''

  def test_image_instance(self):
    self.assertTrue(isinstance(self.new_Image,Image))

  def test_comment_instance(self):
    self.assertTrue(isinstance(self.new_comment,Comments))

  def test_like_instance(self):
    self.assertTrue(isinstance(self.new_like,Likes))

  def test_get_image_by_user(self):
    images = Image.get_images_by_user(self.drew.id)
    self.assertTrue(len(images)>0)

class ProfileTest(TestCase):

  def setUp(self):
    self.drew = User.objects.create_user(username = 'Andrew', password = 'admindrew12345')
   
  def test_update_bio(self):
    self.drew.profile.update_profile_bio("We are the champions")
    self.assertEqual(self.drew.profile.profile_bio,"We are the champions")

  def test_search(self):
    results =Profile.search_user_profile("drew")
    self.assertTrue(len(results)>0)

  def test_get_user_profile(self):
    userprof = Profile.get_user_profile(self.drew)
    self.assertEqual(userprof.user.username,self.drew.username)


class LikesTest(TestCase):
  def setUp(self):
    self.drew = User.objects.create_user(username = 'Andrew', password = 'admindrew12345') 
    self.new_Image = Image(image_name = "Test1", image_caption = "This test works", profile = self.drew.profile, user = self.drew, upload_date = dt.date.today() )
    self.new_Image.image = SimpleUploadedFile(name='travel5.jpg',content=open('/home/martin/Documents/Moringa-Core/Django/InstaClone/Instapic/media/travel5.jpg','rb').read(),content_type='image/jpeg')
    self.new_like = Likes(like=True,user = self.drew, image = self.new_Image)
    self.mary = User.objects.create_user(username = 'Mary', password = 'admindrew12345') 
    self.new_Image.save()
    self.new_like.save()

  def test_get_number_of_likes(self):
    likes_number = Likes.get_number_of_likes(self.new_Image)
    self.assertTrue(likes_number == 1)
  
  def test_like_an_image(self):
    Likes.like_an_image(self.mary,self.new_Image)
    likes_number = Likes.get_number_of_likes(self.new_Image)
    self.assertTrue(likes_number == 2)

  def test_unlike_an_image(self):
    self.new_like.unlike_an_image()
    likes_number = Likes.get_number_of_likes(self.new_Image)
    self.assertTrue(likes_number == 0)
  
  def test_relike_an_image(self):
    self.new_like.relike_an_image()
    likes_number = Likes.get_number_of_likes(self.new_Image)
    self.assertTrue(likes_number == 1)

class CommentsTest(TestCase):
  def setUp(self):
    self.drew = User.objects.create_user(username = 'Andrew', password = 'admindrew12345')
   
    self.new_Image = Image(image_name = "Test1", image_caption = "This test works", profile = self.drew.profile, user = self.drew, upload_date = dt.date.today() )
    self.new_Image.image = SimpleUploadedFile(name='travel5.jpg',content=open('/home/martin/Documents/Moringa-Core/Django/InstaClone/Instapic/media/travel5.jpg','rb').read(),content_type='image/jpeg')
    self.new_comment = Comments(comment = "Amazing", user = self.drew, image = self.new_Image)
    
    self.new_Image.save()
    self.new_comment.save()
    
  def test_get_comemnts_image(self):
    comments = Comments.get_comments_image(self.new_Image)
    self.assertTrue(comments.count() == 1)

  def test_delete_comment(self):
    Comments.delete_comment(self.drew,self.new_Image)
    comments = Comments.get_comments_image(self.new_Image)
    self.assertTrue(comments.count() == 0)
