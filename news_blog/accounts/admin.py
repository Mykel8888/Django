from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin

from .form import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser 

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        'username',
        'age', #new
        'is_staff',
        'name' ,#new
        'date',
        "mike"
        ]

    fieldsets = UserAdmin.fieldsets + ((  None, {'fields':('age','name', 'date', "mike")} ),) # to add age and other fields to default fields

    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields':('age','name', 'date', "mike")}),)

admin.site.register(CustomUser, CustomUserAdmin) #after i use the supeer user to confirm it working
