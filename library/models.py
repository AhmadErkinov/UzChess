from django.db import models

# Create your models here.


class Library(models.Model):

    title = models.CharField(max_length=255)

    auth = models.CharField(max_length=255)

    price = models.CharField(max_length=255)

    reting = models.DecimalField(max_digits=4, decimal_places=2)

    lang = models.CharField(max_length=8)

    sections = models.CharField(max_length=255)

    category = models.CharField(max_length=255)
  
    image = models.FileField(upload_to='library/', blank=True)

    more_button = models.URLField(max_length=255)

    like_buttom = models.BooleanField()
    
