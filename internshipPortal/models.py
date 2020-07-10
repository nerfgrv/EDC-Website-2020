from django.db import models
from django.urls import reverse
from user.models import StartupProfile, StudentProfile
from markdown_deux import markdown
from django.utils.safestring import mark_safe

class Internship(models.Model):
    startup = models.ForeignKey(StartupProfile, on_delete=models.CASCADE, related_name='internships_created', default='')
    field_of_internship = models.CharField(max_length=100, default='')
    duration = models.CharField(max_length=20)
    about = models.TextField()
    location = models.CharField(max_length=100)
    stipend = models.IntegerField()
    skills_required = models.CharField(max_length=500)
    no_of_internships = models.PositiveIntegerField()
    perks = models.CharField(max_length=100)
    who_can_apply = models.CharField(max_length=200)
    applied_by = models.ManyToManyField(StudentProfile, related_name='internships_applied', default='', blank=True)

    def __str__(self):
        return self.startup.startup_name

    def get_absolute_url(self):
        return reverse('internship-detail', kwargs={'pk' : self.pk})

    def about_markdown(self):
        about = self.about
        return mark_safe(markdown(about))


class VentureCapitalist(models.Model):
    company_name = models.CharField(max_length=100)
    about = models.CharField(max_length=5000)
    contact = models.IntegerField()
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.company_name
