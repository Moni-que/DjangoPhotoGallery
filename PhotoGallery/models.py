from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to ='', default='')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField(max_length=500)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    # image_location = models.CharField(max_length=20)

    def __str__(self):
        return self.image_description