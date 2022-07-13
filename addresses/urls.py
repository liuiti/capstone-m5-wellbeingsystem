from django.urls import path
from . import views

urlpatterns = [
    path("address/", views.ListCreateAddressView.as_view()),
    path("address/<pk>/", views.RetrieveUpdateDestroyAddressView.as_view())
]