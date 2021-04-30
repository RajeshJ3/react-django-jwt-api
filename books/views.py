from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import response, status, permissions, authentication
from dj_rest_auth.jwt_auth import JWTCookieAuthentication

from books import models as books_models
from books import serializers as books_serializers


class AuthorViewSet(APIView):

    serializer_class = books_serializers.AuthorSerializer

    def get(self, request):
        qs = books_models.Author.objects.filter(is_active=True)

        serializer = self.serializer_class(qs, many=True)

        output = {
            "detail": "Successful GET request.",
            "output": serializer.data
        }

        return response.Response(output, status.HTTP_200_OK)


class BookViewSet(APIView):

    serializer_class = books_serializers.BookSerializer

    def get(self, request):
        qs = books_models.Book.objects.filter(is_active=True)

        serializer = self.serializer_class(qs, many=True)

        output = {
            "detail": "Successful GET request.",
            "output": serializer.data
        }

        return response.Response(output, status.HTTP_200_OK)
