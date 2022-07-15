from django.urls import path
from . import views

urlpatterns = [
    path("<pk>/avaliations/", views.ListCreateAvaliationView.as_view()),
    path("avaliations/<pk>/", views.RetrieveUpdateDestroyAvaliationView.as_view()),
]
