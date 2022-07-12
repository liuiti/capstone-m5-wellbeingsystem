from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CategorySerializer
from .mixins import SerializerByMethodMixin
from .models import Category
from .permissions import CustomPermission

# Create your views here.

class ListCreateCategoryView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, CustomPermission]

    queryset = Category.objects.all()
    serializer_map = {
        "GET": CategorySerializer,
        "POST": CategorySerializer,
    }

class RetrieveUpdateCategoryView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, CustomPermission]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer