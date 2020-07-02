from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(help_text='Use @ in this field')
	bio = forms.CharField(max_length=500, widget=forms.TextInput({}))
	city = forms.CharField(max_length=40)
	college = forms.CharField(max_length=50)
	resume = forms.URLField(max_length=254)
	contact = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('')}), label=("Phone number"),) 

	class Meta:
	    model = User
	    fields = ['username', 'email', 'password1', 'password2', 'bio', 'city', 'college', 'resume', 'contact']

	def clean(self):
	    email = self.cleaned_data.get('email')

	    if User.objects.filter(username=username).exists():
	        raise forms.ValidationError(
	            "Account with this username already exists")

	    return self.cleaned_data

