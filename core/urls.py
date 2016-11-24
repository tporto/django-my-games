from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    #Home
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    #Games
    url(r'^games/$',views.game_list,name='game_list'),
    url(r'^games/create/$',views.game_create,name='game_create'),
    url(r'^games/(?P<pk>\d+)/update/$', views.game_update, name='game_update'),
    url(r'^games/(?P<pk>\d+)/delete/$', views.game_delete, name='game_delete'),
    #Images
    url(r'^images/create/$',views.create_image,name='image_create'),
    url(r'^images/(?P<pk>\d+)/delete/$', views.image_delete, name='image_delete'),
    url(r'^images/(?P<pk>\d+)/show/$', views.image_show, name='image_show'),
    url(r'^images/$',views.image_list,name='image_list'),
    #url(r'^images/upload/$',views.UploadView.as_view(),name='upload'),
]
