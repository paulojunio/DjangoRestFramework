from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pokemon/$', views.PokemonList.as_view(), name='pokemon-list')
]
