from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.CreateAccountView.as_view()),
    path("accounts/", views.ListAccountView.as_view()),
    path("accounts/<pk>/", views.RetriveUpdateDeleteAccountView.as_view()),
    path("login/", views.LoginView.as_view()),
]
