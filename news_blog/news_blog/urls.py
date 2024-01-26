"""
URL configuration for news_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import views as auth_views

#app_name = 'myapp'

urlpatterns = [
    path('admin/', admin.site.urls),
   path('accounts/', include('accounts.urls')),  # app url()
    
    # Override PasswordChangeView with custom template
    # Include other authentication URLs with custom templates
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('', TemplateView.as_view(template_name='home.html'),  # landing page
         name='home'),]