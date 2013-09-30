# -*- encoding: utf-8 -*-
from django.views.generic  import ListView

from .models import Post
class PostList(ListView):
	template_name="wall/index.html"
	model = Post
	context_object_name = 'posts'

# Create your views here.
