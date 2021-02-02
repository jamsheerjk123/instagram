from django import forms
from .models import UserAccounts
from  django.contrib.auth.forms import  UserCreationForm


class Login(UserCreationForm):
    class Meta:
        model=UserAccounts
        fields=['email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None    
