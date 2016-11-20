from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^games/$',views.game_list,name='game_list'),
    url(r'^games/create/$',views.game_create,name='game_create'),
    url(r'^games/(?P<pk>\d+)/update/$', views.game_update, name='game_update'),
    url(r'^games/(?P<pk>\d+)/delete/$', views.game_delete, name='game_delete'),
]
