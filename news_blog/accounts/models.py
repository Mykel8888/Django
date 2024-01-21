from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


#dodumentation recommend AbstractBaseUser not AbstractUser but its might lead to more complication
#though AbstractBase user has a very fine level of control and custormization but if we want to discuss a model that can be updated with adittiional fields, the better cchoice is abstract 
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True,) 
    name =models.CharField(max_length = 255, null=True, blank = True)
    date = models.DateField(null = True, blank = True)
    mike = models.DateField(null = True, blank = True)  #new

    def __str__ (self):
        return self.username
        


#started from (chapter8 & 9)
#setting --AUTH_USER_MODEL = 'accounts.CustomUser'--
#models
#admin
#migeration
#runserver to check


