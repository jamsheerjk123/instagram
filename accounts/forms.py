from django import forms
from .models import UserAccounts
from django.contrib.auth import get_user_model
from  django.contrib.auth.forms import  UserCreationForm


# class Login(UserCreationForm):
#     class Meta:
#         model=UserAccounts
#         fields=['email']
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         for fieldname in ['email', 'password1', 'password2']:
#             self.fields[fieldname].help_text = None    
class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name']      