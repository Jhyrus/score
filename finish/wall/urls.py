from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import PostList
from .views import ContactView
from .views import InternacionalView
from .views import LpfbView
from .views import MultimediaView
from .views import OpinionView 
from .views import RadioView
from .views import SeleccionView

urlpatterns = patterns('',
    url(r'^$', PostList.as_view(), name='root'),
    url(r'^contact', ContactView.as_view(), name='contact'),
    url(r'^internacional', InternacionalView.as_view(), name='internacional'),
    url(r'^lpfb', LpfbView.as_view(), name='lpfb'),
    url(r'^multimedia', MultimediaView.as_view(), name='multimedia'),
    url(r'^opinion', OpinionView.as_view(), name='opinion'),
    url(r'^radio', RadioView.as_view(), name='radio'),
    url(r'^seleccion', SeleccionView.as_view(), name='seleccion'),
)