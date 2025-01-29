# login_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):    
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    mobile_no = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'mobile_no', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
