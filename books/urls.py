from django.urls import path
from books import views

urlpatterns = [
    path("", views.BookViewSet.as_view()),
    path("authors/", views.AuthorViewSet.as_view()),
]