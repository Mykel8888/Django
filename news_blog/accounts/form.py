from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm

from .models import CustomUser

#Note USer Creation form has an inbuilt django form that contain (name, password, re-password)

class CustomUserCreationForm(UserCreationForm): #to custormise the table from django form defaul(name,password,re-password)
    class Meta (UserCreationForm): # Meta use to overide the default field by setting the model to oour custorm user and using default fields by adding age  metal.fields to include to default fields(age)
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username','email','age','name','date', "mike",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'name', 'date',"mike" )

class CustomPasswordResetForm(PasswordResetForm):
    pass
    # Add your custom form fields or override methods if needed