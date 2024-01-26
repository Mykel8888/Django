from django.urls import path

from .views import SignUpView,PasswordChange
from django.views.generic.base import TemplateView

urlpatterns = [
    path(
        'signup/', SignUpView.as_view(),
        name = 'signup'
    ),
    path("password_change/", PasswordChange.as_view(), name= "password_changes"),
    path('password_change/done', TemplateView.as_view(template_name='registration/password_change_dones.html'), name='my_password_change_done')

]
