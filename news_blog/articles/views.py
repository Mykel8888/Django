from typing import Any
from django.shortcuts import render
from .models import Article

# Create your views here.
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .form import CommentForm
from django.views import View


class ArticlesListView(ListView, LoginRequiredMixin):
    model = Article
    template_name = "article_list.html"

class CommentGet(DetailView):
    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs): # get_context_data() its django dictionary  cantaining all the variable names and value available in our templates, its use to add information to template
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    
class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit = False )
        comment.article = self.object
        comment.save()
        return super().form_valid(form)
    
    def success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})


   

class ArticleDetailView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)



class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #UserPassesTestMixin "pass error annonimous user. only author has access to delete andt to update a post"
    model = Article
    fields = ("title", "body")
    login_url = '/login/'
    template_name = "article_edit.html"


    def test_func(self): #is use to determine if the user has access, if user did not have acces its can be redirect e.g login page login_url = '/login/'
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView,): 
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('home')

    def test_func(self): #only the person that post the post has access to edit and delete file
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView): #loginRequiedMixin redirect user to login when using path
    model = Article
    template_name = "article_new.html"
    fields = ("title", "body",)

#to call for model function or object individually  form.instance.name = "Mike"
    def form_valid(self, form):
        form.instance.author = self.request.user #https://ccbv.co.uk/projects/Django/5.0/django.views.generic.edit/
        return super().form_valid(form)
    
# to make only the person that post have acces to edit and delete post
   
