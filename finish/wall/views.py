# -*- encoding: utf-8 -*-
from django.views.generic import ListView

from .models import Post, Announcement, ImageGalery

class PostList(ListView):
	template_name = "home.html"
	model = Post
	context_object_name = 'posts'

	def get_context_data(self, **kwargs):
		context = super(PostList, self).get_context_data(**kwargs)

		#son los anuncios y las imagenes de las galerias que estan a los costados deberias cargar solo los
		# que entren en la pantalla para eso modifica el la consulta
		context['announcements'] = Announcement.objects.all().order_by("-id")
		context['images'] = ImageGalery.objects.all.order_by("-id")

		return context


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