from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Recipe, Rating
from .serializers import RecipeSerializer, RatingSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
