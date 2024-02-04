from django.urls import path
from .views import SignUpView,PasswordChange, CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView
from django.views.generic.base import TemplateView

urlpatterns = [
    path(
        'signup/', SignUpView.as_view(),
        name = 'signup'
    ),
    path("password_change/", PasswordChange.as_view(), name= "password_changes"),
    path('password_change/done', TemplateView.as_view(template_name='registration/password_change_dones.html'), name='my_password_change_done'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_resets'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
