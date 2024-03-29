from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from addresses.permissions import IsOwnerPermission
from addresses.serializers import AddressSerializer
from .mixins import SerializerByMethodMixin
from .models import Address


class ListCreateAddressView(SerializerByMethodMixin, ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Address.objects.all()
    serializer_map = {
        "GET": AddressSerializer,
        "POST": AddressSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RetrieveUpdateDestroyAddressView(
    SerializerByMethodMixin, RetrieveUpdateDestroyAPIView
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerPermission]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
