from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None):
        user = self.model(email=email, is_staff=True, is_superuser=True)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email Address', unique=True)
    is_student = models.BooleanField(default=False)
    is_startup = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name ='student_profile')
    name = models.CharField(max_length=60, default='')
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=40, default='')
    college = models.CharField(max_length=50)
    resume = models.URLField(default='')
    contact = PhoneNumberField()

    def __str__(self):
        return self.user.email


class StartupProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name = 'startup_profile')
    startup_name = models.CharField(max_length=40, default='')
    about = models.TextField(max_length=500, blank=True)
    founder = models.CharField(max_length=150, default='')
    city = models.CharField(max_length=40, default='')
    field_of_work = models.CharField(max_length=50)
    website = models.URLField(default='')
    contact = PhoneNumberField()
    image = models.ImageField(default='default.jpg', upload_to='startup/')

    def __str__(self):
        return self.user.email
