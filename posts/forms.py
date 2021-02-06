from django import forms
from .models import POSTS

class PostAddForm(forms.ModelForm):
    class Meta:
        model = POSTS
        fields = ['image','caption']