from django.db import models
from course.models import Course
from library.models import Library
# Create your models here.


class MyProfile(models.Model):

    name = models.CharField(max_length=255)

    image = models.FileField(upload_to='myProfile_me/', blank=True)

    purchased_courses = models.ForeignKey(Course, on_delete=models.CASCADE)

class Order(models.Model):

    order_number = models.CharField(max_length=255)

    order_status = models.CharField(max_length=255)

    order_price = models.CharField(max_length=255)

    ordered_things = models.CharField(max_length=255)

    order_image = models.FileField(upload_to='myProfile_me', blank=True)

class Saved(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    books = models.ForeignKey(Library, on_delete=models.CASCADE)

class Settings(models.Model):

    user_firs_name = models.CharField(max_length=255)
    user_second_name = models.CharField(max_length=255)
    user_both_date = models.CharField(max_length=255)
    # user_password = models.CharField(max_length=255)
    user_phonenumber = models.CharField(max_length=16)