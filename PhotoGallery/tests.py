from django.test import TestCase
from .models import Image,Category
import datetime as dt

# Create your tests here.
class ImageTestClass(TestCase):

    #set up method
    def setUp(self):
        self.myimage = Image(image_name = 'Travel', image_description = 'This is my travel image')

     #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.myimage,Image))

    #Testing Save Method
    def test_save_method(self):
        self.myimage.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        # self.myimage = Image(image_name = 'Travel', image_description = 'This is my travel image')

        self.new_category = Category(name = 'testing')
        self.new_category.save()


    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
