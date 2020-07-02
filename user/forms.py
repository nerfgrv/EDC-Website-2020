from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	bio = forms.CharField(max_length=500, widget=forms.TextInput({}), required=False)
	city = forms.CharField(max_length=40)
	college = forms.CharField(max_length=50)
	resume = forms.URLField(max_length=254)
	contact = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('')}), label=("Phone number"), required=False) 

	class Meta:
	    model = User
	    fields = ['username', 'email', 'password1', 'password2', 'bio', 'city', 'college', 'resume', 'contact']

	def clean(self):
	    email = self.cleaned_data.get('email')
	    contact = self.cleaned_data.get('contact')
	    username = self.cleaned_data.get('username')

	    if User.objects.filter(username=username).exists():
	        raise forms.ValidationError(
	            "Account with this username already exists")
	    if User.objects.filter(email=email).exists():
	        raise forms.ValidationError(
                "Account with this email already exists")
	    # if User.objects.filter(contact=contact).exists():
	    #     raise forms.ValidationError(
     #            "Account with this contact number already exists")

	    return self.cleaned_data

