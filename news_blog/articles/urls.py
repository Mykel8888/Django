from django.urls import path
from .views import (ArticlesListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView,ArticleDeleteView )

urlpatterns = [
    
    path("<int:pk>/", ArticleDetailView.as_view(), name = "article_detail"),
    path ("<int:pk>/edit/", ArticleUpdateView.as_view(), name = "article_edit"),
    path ("<int:pk>/delete/", ArticleDeleteView.as_view(), name = "article_delete"),
    path ("newpost/", ArticleCreateView.as_view(), name = "new_article"),
    path("", ArticlesListView.as_view(), name ='article_list'),
]