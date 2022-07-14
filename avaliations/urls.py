from django.urls import path
from . import views

urlpatterns = [
    path("avaliation/", views.ListCreateAvaliationView.as_view()),
    path("avaliation/<pk>/", views.RetrieveUpdateDestroyAvaliationView.as_view()),
]
