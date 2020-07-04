from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction
from .models import User, StudentProfile, StartupProfile

class StudentRegisterForm(UserCreationForm):
	email 	= forms.EmailField()
	bio 	= forms.CharField(max_length=500, widget=forms.TextInput({}), required=False)
	city 	= forms.CharField(max_length=40)
	college = forms.CharField(max_length=50)
	resume 	= forms.URLField(max_length=254)
	contact = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('')}), label=("Phone number"), required=False) 
	
	class Meta(UserCreationForm.Meta):
		model 	= User
		fields 	= ['username', 'email', 'contact', 'college', 'city', 'bio', 'resume',  'password1', 'password2']
	
	@transaction.atomic
	def clean(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		
		if student.objects.filter(username=username).exists():
			raise forms.ValidationError("Account with this username already exists")
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Account with this email already exists")
		return self.cleaned_data


class StartupRegisterForm(UserCreationForm):
    startupname = forms.CharField(max_length=40)
    email = forms.EmailField()
    about = forms.CharField(max_length=500, widget=forms.TextInput({}), required=False)
    city = forms.CharField(max_length=40)
    fieldofwork = forms.CharField(max_length=50)
    website = forms.URLField(max_length=254)
    image = forms.ImageField()
    contact = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('')}), label=("Phone number"), required=False)
	
    class Meta():	
        model = User
        fields = ['startupname', 'username', 'email', 'contact', 'about',  'city', 'fieldofwork', 'website', 'image', 'password1','password2']

    @transaction.atomic
    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
		
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Account with this username already exists")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Account with this email already exists")
        return self.cleaned_data
