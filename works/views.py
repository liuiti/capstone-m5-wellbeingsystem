from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import WorkSerializer, ListWorksSerializer
from .mixins import SerializerByMethodMixin
from .models import Work
from .permissions import CustomPermission, IsOwnerPermission



class ListCreateWorkView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, CustomPermission]

    queryset = Work.objects.all()
    serializer_map = {
        "GET": ListWorksSerializer,
        "POST": WorkSerializer,
    }

    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)

class RetrieveUpdateDestroyWorkView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerPermission]

    queryset = Work.objects.all()
    serializer_class = WorkSerializer