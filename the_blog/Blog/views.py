from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import BlogPost
from .forms import BlogPostForm

#def home(request):
   # return render(request, 'home.html', {})

#listview for showing all our blogpost on homepage
class  HomeView(ListView):
    model = BlogPost
    template_name = 'home.html'

#putting one post on a page 
class ArticleDetailView(DetailView):
    model = BlogPost
    template_name = 'article_details.html'

#must be able to create a new post
class AddPostView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ['title', 'content']


class EditPostView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'update_post.html'
    #fields = ['content', 'title_tag', 'title']