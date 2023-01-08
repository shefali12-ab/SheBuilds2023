from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget
from .models import *

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class AddDiscussion(ModelForm):
    class Meta:
        model = DiscussionModel
        fields = ['title', 'topic', 'description']

class AddComment(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment']

