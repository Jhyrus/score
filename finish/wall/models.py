# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#
#GENERALES
#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#
class LabelModel(models.Model):
    label = models.CharField(max_length=50)

    def __unicode__(self):
        return self.label

class Autor(models.Model):
    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to="Autores")

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __unicode__(self):
        return self.user.username


class Category(LabelModel):
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#
#PUBLICIDAD
#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#

class Announcement(models.Model):
    POSITION_CHOICES = (
        ("Arriba", "top"),
        ("Centro", "center"),
        ("Izquierda", "left"),
        ("Derecha", "right"),
    )

    def save_to(self, filename):
        ruta = "uploads/ads/images/%s" % filename
        return ruta

    title = models.CharField(max_length=40)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    size = models.IntegerField()
    date = models.DateField()
    image = models.ImageField(upload_to=save_to)

    class Meta:
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'

    def __unicode__(self):
        return "%s" % self.title

class Banner(models.Model):

    def save_to(self, filename):
        ruta = "uploads/banners/images/%s" % filename
        return ruta

    title = models.CharField(max_length=40)
    date = models.DateField()
    image = models.ImageField(upload_to=save_to)
    link = models.CharField(max_length=400)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __unicode__(self):
        return "%s" % self.title


#------------------------------------------------------------------------------------------#
#PUBLICACION
#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#

class Caricatura(models.Model):
    def save_to(self, filename):
        ruta = "uploads/caricaturas/images/%s" % (filename)
        return ruta

    autor = models.ForeignKey('Autor')
    image = models.ImageField(upload_to=save_to)
    title = models.CharField(max_length=30)
    date = models.DateField()

    class Meta:
        verbose_name = 'Caricatura'
        verbose_name_plural = 'Caricaturas'

    def __unicode__(self):
        return self.title


class Video(models.Model):
    def url_video(self, filename):
        ruta = "uploads/videos/%s" % (filename)
        return ruta

    def url_preload(self, filename):
        ruta = "uploads/videos/preloads/%s" % (filename)
        return ruta

    title= models.CharField(max_length=60)
    category = models.ForeignKey('Categoria'),
    description = models.CharField(max_length=100)
    video = models.FileField(upload_to=url_video)
    preload = models.ImageField(upload_to=url_preload)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __unicode__(self):
        return self.title

#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#
#Noticias
#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#
class TypePost(LabelModel):
    class Meta:
        verbose_name = 'Tipo de Publicación'
        verbose_name_plural = 'Tipos de Publicaciónes'

class Post(models.Model):
    def save_to(self, filename):
        ruta = "uploads/posts/images/%s" % (filename)
        return ruta

    title = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor')
    category = models.ForeignKey('Category')
    content = models.TextField(max_length=7500)
    image = models.ImageField(upload_to=save_to)
    date = models.DateField()
    visible = models.BooleanField(default=True)
    type = models.ForeignKey('TypePost')

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

    def __unicode__(self):
        return self.title

#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#
#FRASE DEL DIA
#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#

class Phrase(models.Model):
    autor = models.CharField(max_length=100)
    phrase = models.CharField(max_length=120)
    date = models.DateField()

    class Meta:
        verbose_name = 'Frase'
        verbose_name_plural = 'Frases'

    def __unicode__(self):
        return self.phrase

#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#
#GALERIAS
#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#

class TypeGalery(LabelModel):
    class Meta:
        verbose_name = 'Tipo de Galería'
        verbose_name_plural = 'Tipos de Galerías'


class ImageGalery(models.Model):
    class Meta:
        verbose_name_plural = "Imagenes"

    def url(self, filename):
        ruta = "uploads/slides/%s" % (filename)
        return ruta

    autor = models.ForeignKey('Autor')
    category = models.ForeignKey('Category')
    description = models.TextField(max_length=500)
    date = models.DateField()
    galery = models.ForeignKey('TypeGalery')
    image = models.ImageField(upload_to=url)
    title = models.CharField(max_length=200)
    visible = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Imagen de Galería'
        verbose_name_plural = 'Imagenes de Galerias'

    def __unicode__(self):
        return self.title

#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#
#ANUNCIANTE
#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#

class Sponsor(models.Model):
    def url_img(self, filename):
        ruta = "uploads/videos/preloads/%s" % filename

    name = models.CharField(max_length=80)
    logo = models.ImageField(upload_to=url_img)
    link = models.CharField(max_length=400)

    class Meta:
        verbose_name = 'Anunciante'
        verbose_name_plural = 'Anunciantes'

    def __unicode__(self):
        return self.name

