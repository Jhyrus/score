from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import PostList

urlpatterns = patterns('',
    url(r'^$', PostList.as_view(), name='root'),
)