from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


    def save_image(self):
        self.save()
        

# class Location(models.Model):
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name

class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField(max_length=500)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    # image_location = models.ForeignKey(Location, on_delete=models.CASCADE, default='')


    def save_category(self):
        self.save()

    @classmethod
    def search_by_category(cls, category_term):
        gallery = cls.objects.filter(name__icontains=category_term)
        return gallery


    def __str__(self):
        return self.image_description