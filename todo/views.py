from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm

class TodoListView(ListView):
    model = Post
    template_name = "home.html"

class TodoCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body", "deadline"]
    
class TodoUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    form_class = PostForm
    
class TodoDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")