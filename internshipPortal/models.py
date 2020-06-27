from django.db import models


# Create your models here.
class Internship(models.Model):
    company_name = models.CharField(max_length=100)
    fields_of_work = models.CharField(max_length=1000)
    duration = models.CharField(max_length=20)
    about = models.CharField(max_length=5000)
    location = models.CharField(max_length=100)
    stipend = models.IntegerField()
    skills_required = models.CharField(max_length=500)
    no_of_internships = models.IntegerField()
    perks = models.CharField(max_length=100)
