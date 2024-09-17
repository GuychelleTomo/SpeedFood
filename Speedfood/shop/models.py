from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length= 255)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    disponible = models.BooleanField(default=False)
    thumbnails = models.ImageField(blank=True, null=True, upload_to="media")


class Cart(models.Model):
    pass
