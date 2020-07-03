from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_startup = models.BooleanField(default=False)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name ='student_profile')
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=40, default='')
    college = models.CharField(max_length=50)
    resume = models.URLField(default='')
    email = models.EmailField(max_length=254)
    contact = PhoneNumberField()

    def __str__(self):
        return self.user.username


class StartupProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name = 'startup_profile')
    name = models.CharField(max_length=40, default='')
    about = models.TextField(max_length=500, blank=True)
    founder = models.CharField(max_length=40, default='')
    city = models.CharField(max_length=40, default='')
    fieldofwork = models.CharField(max_length=50)
    website = models.URLField(default='')
    email = models.EmailField(max_length=254)
    contact = PhoneNumberField()

    def __str__(self):
        return self.user.username
