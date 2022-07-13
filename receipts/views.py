from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
)
from .models import Receipt
from .serializers import PayedSerializer, ReceiptSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from works.models import Work
from accounts.permissions import IsSuperuserOrReadOnly
from .permission import IsConstractorPermission


class ListCreateReceiptView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    def perform_create(self, serializer):
        work = get_object_or_404(Work, pk=self.kwargs["pk"])
        serializer.save(contractor=self.request.user, works=work)


class RetrieveUpdateReceiptView(RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]

    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer


class UpdatePayed(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsConstractorPermission]

    queryset = Receipt.objects.all()
    serializer_class = PayedSerializer
