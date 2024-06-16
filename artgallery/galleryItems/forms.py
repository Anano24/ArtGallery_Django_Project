from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from .models import GalleryItems
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory



class GalleryItemsForm(forms.ModelForm):

    class Meta:
        model = GalleryItems

        fields = ['title', 'description', 'price', 'categories', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter the description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the price'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

