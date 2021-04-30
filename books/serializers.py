from django.db.models import fields
from rest_framework import serializers
from books import models as books_models

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = books_models.Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = books_models.Book
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({
            "author_name": instance.author.name
        })
        return data
