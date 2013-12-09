# -*- encoding: utf-8 -*-
from django.contrib import admin
from finish.wall.models import (Autor, Category, Announcement, Banner, Caricatura,
                                Video, TypePost, Post, Phrase, TypeGalery,
                                ImageGalery, Sponsor)


class AutorAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class AnnouncementAdmin(admin.ModelAdmin):
    pass

class BannerAdmin(admin.ModelAdmin):
    pass

class CaricaturaAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass


class TypePostAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('admin/js/tiny_mce/tiny_mce.js',
              'admin/js/tiny_mce/basic_config.js',)


class PhraseAdmin(admin.ModelAdmin):
    pass


class TypeGaleryAdmin(admin.ModelAdmin):
    pass


class ImageGaleryAdmin(admin.ModelAdmin):
    pass


class SponsorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Autor, AutorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Caricatura, CaricaturaAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(TypePost, TypePostAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Phrase, PhraseAdmin)
admin.site.register(TypeGalery, TypeGaleryAdmin)
admin.site.register(ImageGalery, ImageGaleryAdmin)
admin.site.register(Sponsor, SponsorAdmin)

