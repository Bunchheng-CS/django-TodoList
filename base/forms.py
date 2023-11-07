from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TodoTask


class TodoTaskForm(ModelForm):
    class Meta:
        model = TodoTask
        fields = ['title', 'description', 'complete']
        widgets = {
            'title': forms.TextInput(attrs={ 'placeholder': 'Title...','style':"font-size:1.1rem;margin-left:0.5rem;", }),
            'description': forms.Textarea(attrs={ "rows": "3",'style':"font-size:1.1rem;margin-left:0.5rem;",}),
            'complete': forms.CheckboxInput(attrs={ 'style':"font-size:1.1rem;margin-left:0.5rem;",}),
        }


class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
       
