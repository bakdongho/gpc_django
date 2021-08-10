from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib import messages
from user.forms import CustomUserCreationForm

# Create your views here.

class UserRegistrationView(CreateView):
    model=get_user_model()
    success_url='/article/'
    form_class=CustomUserCreationForm

class UserLoginView(LoginView):
    template_name = 'user/login_form.html'
    def form_invalid(self, form) -> HttpResponse:
        messages.error(self.request, 'login fail',extra_tags='danger')
        return super().form_invalid(form)