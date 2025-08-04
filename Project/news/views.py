from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']  # Сортировка от новых к старым
    queryset = Post.objects.filter(post_type='NW')  # Только новости

class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

class ArticleList(ListView):
    model = Post
    template_name = 'news/article_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    queryset = Post.objects.filter(post_type='AR')

class ArticleDetail(DetailView):
    model = Post
    template_name = 'news/article_detail.html'
    context_object_name = 'article'