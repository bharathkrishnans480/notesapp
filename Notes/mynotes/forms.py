from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from mynotes.models import Notes





class MyNotesForm(ModelForm):
    class Meta:
        model=Notes
        fields=[
            'title',
            'description',
            'image',
        ]

        widgets={
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),

        }