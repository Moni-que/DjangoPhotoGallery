from django.db import models

# Create your models here.
class Image(models.Model):
    # image = models.ImageField(upload_to ='/')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField(max_length=150)
    image_category = models.CharField(max_length=30)
    image_location = models.CharField(max_length=20)



# class Location(models.Model):



# class Category(models.Model):

