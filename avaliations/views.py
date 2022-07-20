from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from avaliations.permissions import IsOwnerPermission
from avaliations.serializers import AvaliationSerializer
from .mixins import SerializerByMethodMixin
from .models import Avaliation
from receipts.models import Receipt


class ListCreateAvaliationView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer

    def perform_create(self, serializer):
        receipt = get_object_or_404(Receipt, pk=self.kwargs["pk"])
        serializer.save(receipt=receipt)


class RetrieveUpdateDestroyAvaliationView(
    SerializerByMethodMixin, RetrieveUpdateDestroyAPIView
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerPermission]

    queryset = Avaliation.objects.all()
    serializer_map = {
        "GET": AvaliationSerializer,
        "POST": AvaliationSerializer,
        }
