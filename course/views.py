from django.shortcuts import render
from course.models import Course
from rest_framework import filters
from course.serializers import CourseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

# class UserListView(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     filter_backends = [filters.OrderingFilter]
#     search_fields = ['daraja', 'kategoriya', 'darslik tili', 'reyting']

class CourseView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer