from django.test import TestCase
from .models import User,Image,Comments,Profile
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests here.

class ImageTest(TestCase):

  def setUp(self):
    self.drew = User.objects.create_user(username = 'Andrew', password = 'admindrew12345')
   
    self.new_Image = Image(image_name = "Test1", image_caption = "This test works", profile = self.drew.profile, user = self.drew,likes = 1)
    self.new_Image.image = SimpleUploadedFile(name='travel5.jpg',content=open('/home/martin/Documents/Moringa-Core/Django/InstaClone/Instapic/media/travel5.jpg','rb').read(),content_type='image/jpeg')
    self.new_comment = Comments(comment = "Amazing", user = self.drew, image = self.new_Image)
   
    self.new_Image.save()
    self.new_comment.save()
    '''
    Tests
    '''

  def test_image_instance(self):
    self.assertTrue(isinstance(self.new_Image,Image))

  def test_comment_instance(self):
    self.assertTrue(isinstance(self.new_comment,Comments))

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


