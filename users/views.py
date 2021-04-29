from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication

class TestView(APIView):

    def get(self, request):
        output = {
            "detail": "SUCCESS!"
        }
        return Response(output, status.HTTP_200_OK)
