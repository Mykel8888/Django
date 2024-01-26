from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeView

from .form import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('my_password_change_done')
    template_name = 'registration/password_change_forms.html'

