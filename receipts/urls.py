from django.urls import path
from . import views

urlpatterns = [
    path("<pk>/receipts/", views.ListCreateReceiptView.as_view()),
    path("receipts/<pk>/", views.RetrieveUpdateDestroyReceiptView.as_view()),
]
