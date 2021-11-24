from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Article
from .forms import ArticleModelForm
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView    
)

# Create your views here.
# using class-based views

class ArticleListView(ListView):
    # custom template
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() # generic template - <blog>/<modulename>_list.html

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # overides the default redirect after creating the item
    # def get_success_url(self):
    #     return '/' # some path

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    # queryset = Article.objects.all() # limits the scope of the view

    # this functions overides pk to id
    # when using this function, the queryset can be omitted
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    # queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')
