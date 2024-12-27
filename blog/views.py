from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

class PageListView(ListView):
    model = Post
    template_name = 'blog/pages_list.html'
    context_object_name = 'posts'

class PageDetailView(DetailView):
    model = Post
    template_name = 'blog/page_detail.html'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/page_form.html'
    fields = ['title', 'subtitle', 'content', 'image']
    success_url = reverse_lazy('pages_list')

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/page_form.html'
    fields = ['title', 'subtitle', 'content', 'image']
    success_url = reverse_lazy('pages_list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/page_confirm_delete.html'
    success_url = reverse_lazy('pages_list')
