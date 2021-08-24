from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from Log.models import Book


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)


class BooksForm(forms.ModelForm):
    class Meta:
        model =Book
        fields =('title','author','pdf')
