from django.db import models
from django.urls import reverse

# Create your models here.
class Investor(models.Model):
    company_name = models.CharField(max_length=100)
    about = models.CharField(max_length=5000)
    contact = models.IntegerField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.company_name
