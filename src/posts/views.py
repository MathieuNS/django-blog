from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from posts.models import BlogPost

class BlogHome(ListView):
    model = BlogPost
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)

@method_decorator(login_required, name='dispatch' )
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = 'posts/blogpost_create.html'
    fields = ['title', 'content', ]

@method_decorator(login_required, name='dispatch' )
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = 'posts/blogpost_update.html'
    fields = ['title', 'content', 'published',]

class BlogPostView(DetailView):
    model = BlogPost
    template_name = 'posts/blogpost_view.html'
    context_object_name = 'post'

@method_decorator(login_required, name='dispatch' )
class BlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('posts:home')

def blog(request):
    return redirect("/blog/")