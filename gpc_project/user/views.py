from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

from user.forms import CustomUserCreationForm

# Create your views here.

class UserRegistrationView(CreateView):
    model=get_user_model()
    success_url='/article/'
    form_class=CustomUserCreationForm
