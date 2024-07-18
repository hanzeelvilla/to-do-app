from django.urls import path
from .views import (
    TodoListView, 
    TodoCreateView, 
    TodoUpdateView, 
    TodoDeleteView,
)

urlpatterns = [
    path("post/new/", TodoCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", TodoUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", TodoDeleteView.as_view(), name="post_delete"),
    path("", TodoListView.as_view(), name="home"),
]