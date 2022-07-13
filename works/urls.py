from django.urls import path
from . import views

urlpatterns = [
    path("works/", views.ListCreateWorkView.as_view()),
    path("works/<pk>/", views.RetrieveUpdateDestroyWorkView.as_view()),
]
