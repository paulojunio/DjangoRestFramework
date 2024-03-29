from django.shortcuts import render
from rest_framework import generics
from .models import Pokemon
from .serializers import PokemonSerializer

# Create your views here.


class PokemonList(generics.ListCreateAPIView):

    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
