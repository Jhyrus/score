# -*- encoding: utf-8 -*-
from django.views.generic import ListView
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from finish.wall.models import Post
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404

from .models import Post, Announcement, ImageGalery, Caricatura, Phrase, Video, Banner

class PostList(ListView):
	template_name = "home.html"
	model = Post
	context_object_name = 'posts'

	def get_context_data(self, **kwargs):
		context = super(PostList, self).get_context_data(**kwargs)

		#son los announcements y las imagenes de las galerias que estan a los costados deberias cargar solo los
		# que entren en la pantalla para eso modifica el la consulta
		context['announcements'] = Announcement.objects.all().order_by("-id")
		context['images'] = ImageGalery.objects.all().order_by("-id")
		context['caricatura'] = Caricatura.objects.all().order_by("-id")
		context['frase'] = Phrase.objects.all().order_by("-id")
		context['posts'] = Post.objects.all().order_by("-id")
		return context

class PostDetailView(DetailView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['announcements'] = Announcement.objects.all().order_by("-id")
        context['posts'] = Post.objects.all().order_by("-id")
        context['banner'] = Banner.objects.all().order_by("-id")
        return context




def listing(request):
    announcements = Announcement.objects.all().order_by("-id")
    post = Post.objects.all().order_by('-id')
    frase = Phrase.objects.all().order_by('-id')
    caricatura = Caricatura.objects.all().order_by('-id')
    titulares = Post.objects.all().order_by('-id')
    titulares = Post.objects.all().order_by('-id')

    paginator1 = Paginator(announcements, 14)
    paginator2 = Paginator(post, 10)
    paginator3 = Paginator(frase, 1)
    paginator4 = Paginator(caricatura, 1)
    paginator5 = Paginator(titulares, 4)

    if request.GET.get('page1'):
        request.session['page1'] = request.GET.get('page1')

    if request.GET.get('page2'):
        request.session['page2'] = request.GET.get('page2')

    if request.GET.get('page3'):
        request.session['page3'] = request.GET.get('page3')

    if request.GET.get('page4'):
        request.session['page4'] = request.GET.get('page4')

    if request.GET.get('page5'):
        request.session['page5'] = request.GET.get('page5')

    try:
        page1 = int(request.session.get('page1', 1))
        page2 = int(request.session.get('page2', 1))
        page3 = int(request.session.get('page3', 1))
        page4 = int(request.session.get('page4', 1))
        page5 = int(request.session.get('page5', 1))
    except ValueError:
        page1 = page2 = page3 = page4 = page5 = 1

    try:
        announcements = paginator1.page(page1)
        post = paginator2.page(page2)
        frase = paginator3.page(page3)
        caricatura = paginator4.page(page4)
        titulares = paginator5.page(page5)
    except (EmptyPage, InvalidPage):
        announcements = paginator1.page(paginator1.num_pages)
        post = paginator2.page(paginator2.num_pages)
        frase = paginator3.page(paginator3.num_pages)
        caricatura = paginator4.page(paginator4.num_pages)
        titulares = paginator5.page(paginator5.num_pages)

    return render(request, 'home.html', {
        'announcements': announcements,
        'post': post,
        'frase': frase,
        'caricatura': caricatura,
        'titulares': titulares
    })


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

