from django.urls import path
from users import views

urlpatterns = [
    path("test/", views.TestView.as_view()),
]
