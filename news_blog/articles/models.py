from django.db import models
from django.conf import settings
# Create your models here.
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=55)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,) #author =models.ForeignKey('auth.User', on_delete=models.CASCADE,)



    def __str__(self):
        return self.title #display the data title in admin page
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,) #author =models.ForeignKey('auth.User', on_delete=models.CASCADE,)



    def __str__(self):
        return self.comment #display the data title in admin page
    
    def get_absolute_url(self):
        return reverse('article_list', kwargs={'pk': self.pk})
    
    

    #this is where our editing will be land

#immidiate after this i need to make migeration before import to form "python manage.py makemigrations articles" then "python manage.py migrate"