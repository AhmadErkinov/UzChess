from rest_framework import serializers
from main.models import Main

class LibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Main
        fields = ("id", "title", "auth", "price", "reting", "lang", "sections", "category", "image")