from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product')
    description = models.TextField()
    hard_ware = models.TextField()
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(150, 150)], 
                                    format='JPEG',
                                   )

    def __str__(self):
        return self.name