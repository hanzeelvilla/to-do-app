from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm

class TodoListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "home.html"
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_new.html"
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TodoUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "post_edit.html"
    form_class = PostForm
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class TodoDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user