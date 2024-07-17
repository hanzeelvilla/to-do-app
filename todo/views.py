from django.views.generic import ListView, DetailView
from .models import Post

class TodoListView(ListView):
    model = Post
    template_name = "home.html"
