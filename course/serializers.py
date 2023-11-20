from rest_framework import serializers
from course.models import Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "title", "auth", "price", "reting", "lang", "sections", "degree", "category", "image")