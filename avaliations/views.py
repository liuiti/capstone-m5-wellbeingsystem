from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from avaliations.permissions import IsOwnerPermission
from avaliations.serializers import AvaliationSerializer
from .mixins import SerializerByMethodMixin
from .models import Avaliation


class ListCreateAvaliationView(SerializerByMethodMixin, ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RetrieveUpdateDestroyAvaliationView(
    SerializerByMethodMixin, RetrieveUpdateDestroyAPIView
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer
