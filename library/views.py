from django.shortcuts import render
from library.serializers import LibrarySerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import filters
from .models import Library

# class UserListView(generics.ListAPIView):
#     queryset = Library.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = [filters.OrderingFilter]
#     search_fields = ['tili', 'kategoriya', 'daraja', 'reyting']

class LibraryView(generics.ListAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer