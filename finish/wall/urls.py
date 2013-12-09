from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import PostList
from .views import ContactView
from .views import InternacionalView
from .views import LpfbView
from .views import MultimediaView
from .views import OpinionView
from .views import RadioView
from .views import SeleccionView
from .views import Post
from finish.wall.views import PostDetailView

urlpatterns = patterns('',
    url(r'^$',  'finish.wall.views.listing', name='post'),
    url(r'^contact', ContactView.as_view(), name='contact'),
    url(r'^internacional', InternacionalView.as_view(), name='internacional'),
    url(r'^lpfb', LpfbView.as_view(), name='lpfb'),
    url(r'^multimedia', MultimediaView.as_view(), name='multimedia'),
    url(r'^opinion', OpinionView.as_view(), name='opinion'),
    url(r'^radio', RadioView.as_view(), name='radio'),
    url(r'^seleccion', SeleccionView.as_view(), name='seleccion'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post'),
    url(r'^pagi', 'finish.wall.views.listing', name='post'),
)