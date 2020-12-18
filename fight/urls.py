from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^role_list/$', views.role_list, name='role_list'),
    url(r'^role_vs/$', views.role_vs, name='role_vs'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
