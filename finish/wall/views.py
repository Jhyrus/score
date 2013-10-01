# -*- encoding: utf-8 -*-
from django.views.generic import ListView

from .models import Post

class PostList(ListView):
	template_name = "home.html"
	model = Post
	context_object_name = 'posts'

# Create your views here.


class ContactView(ListView):
	template_name = "wall/index.html"
	model = Post
	context_object_name = 'posts'
	paginate_by = 6


class InternacionalView(ListView):
	template_name = "wall/internacional.html"
	model = Post
	context_object_name = 'contact'


class LpfbView(ListView):
	template_name = "wall/lpfb.html"
	model = Post
	context_object_name = 'lpfb'


class MultimediaView(ListView):
	template_name = "wall/multimedia.html"
	model = Post
	context_object_name = 'multimedia'


class OpinionView(ListView):
	template_name = "wall/opinion.html"
	model = Post
	context_object_name = 'opinion'


class RadioView(ListView):
	template_name = "wall/radio.html"
	model = Post
	context_object_name = 'radio'


class SeleccionView(ListView):
	template_name = "wall/seleccion.html"
	model = Post
	context_object_name = 'seleccion'