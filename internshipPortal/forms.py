from django import forms
from .models import Internship


class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = [
            'company_name',
            'fields_of_work',
            'duration',
            'about',
            'location',
            'stipend',
            'skills_required',
            'no_of_internships',
            'perks',
            'who_can_apply'
        ]
