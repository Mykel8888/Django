from django.contrib import admin

# Register your models here.
from .models import Article, Comment
from django.contrib import admin

# to modify dmin comment display
class CommentInLine(admin.TabularInline): #admin.StackedInline "each field has its  own line". admin.TabularInline "all the model apear in one line"
    model = Comment
    #extra = 0
class ArticleAdmin(admin.ModelAdmin):
    #new
    inlines = [ CommentInLine ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)