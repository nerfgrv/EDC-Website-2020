from django.db import models


# Create your models here.
class Internship(models.Model):
    company_name = models.CharField(max_length=100)
    fields_of_work = models.CharField(max_length=1000)
    duration = models.CharField(max_length=20)
    about = models.CharField(max_length=5000)
    location = models.CharField(max_length=100)
    stipend = models.CharField(max_length=25)
    skills_required = models.CharField(max_length=500)
    no_of_internships = models.IntegerField()
    perks = models.CharField(max_length=100)
    who_can_apply = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name


class VentureCapitalist(models.Model):
    company_name = models.CharField(max_length=100)
    about = models.CharField(max_length=5000)
    contact = models.IntegerField()
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.company_name
