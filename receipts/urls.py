from django.urls import path
from . import views

urlpatterns = [
    path("<pk>/receipts/", views.CreateReceiptView.as_view()),
    path("receipts/<pk>/", views.RetrieveUpdateReceiptView.as_view()),
    path("receipts/<pk>/pay/", views.UpdatePayed.as_view()),
    path("receipts/users/<pk>/", views.ListUsersFromReceipts.as_view()),
]
