from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
   queryset = Post.objects.all()
   template_name = "blog/post_list.html"

# django classes used to display list of objects
detailview = generic.DetailView
createview = generic.CreateView
updateview = generic.UpdateView  