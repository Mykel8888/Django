from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeView,PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .form import CustomUserCreationForm,CustomPasswordResetForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('my_password_change_done')
    template_name = 'registration/password_change_forms.html'


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_forms.html'
#email_template_name = 'custom_password_reset_email.txt'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_dones.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirms.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_completes.html'
