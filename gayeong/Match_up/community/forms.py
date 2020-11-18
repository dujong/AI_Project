from django import forms
from .models import *
from django.forms.widgets import ClearableFileInput

class Community_Form(forms.ModelForm):
    class Meta:
        model = Community_Post
        fields = ('title', 'title_image', 'content')
        labels = {
            'title': '',
            'title_image': '',
            'content': '',
        }
        