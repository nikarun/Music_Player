from django.forms import ModelForm
from .models import *
from django import forms
class Add_Album_form(ModelForm):
    class Meta:
        model=Album
        widgets={
            "name":" ",
            "director": " ",
            "image": " "
        }

