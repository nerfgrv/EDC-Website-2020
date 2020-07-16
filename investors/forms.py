from django import forms
from .models import Investor
from user.models import StartupProfile


class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = [
            'name',
            'about',
            'startups_funded',
            'contact',
            'email',
            'photo',
        ]    

class StartupProfileForm(forms.ModelForm):
    class Meta:
        model = StartupProfile
        fields = [
            'startup_name',
            'about_the_startup',
            'founders',
            'field_of_work',
            'website',
            'photo',
        ]    