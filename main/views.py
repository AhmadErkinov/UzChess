from django.shortcuts import render
from library.serializers import LibrarySerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import filters
from .models import Main


class MainView(generics.ListAPIView):
    queryset = Main.objects.all()
    serializer_class = LibrarySerializer