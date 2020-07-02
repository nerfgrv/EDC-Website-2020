from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=40, default='')
    college = models.CharField(max_length=50)
    resume = models.URLField(default='')
    email = models.EmailField(max_length=254)
    contact = PhoneNumberField()
    
    # class Meta:
    #     db_table ="student"

    def __str__(self):
        return self.user.username
