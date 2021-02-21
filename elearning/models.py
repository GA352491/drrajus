from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings


class Payment(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, default='')
    course = models.CharField(max_length=100, null=True)
    secondary_course = models.CharField(max_length=100, null=True)
    amount = models.IntegerField(null=True)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    date_of_payment = models.DateField(null=True)

    def __str__(self):
        return self.user_name


class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.course_name


from tinymce import HTMLField


class Blog(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    overview = models.TextField(max_length=400, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField('Content')
    thumbnail = models.ImageField(upload_to='Blog')

    def __str__(self):
        return self.title
