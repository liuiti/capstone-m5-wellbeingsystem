from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Receipt
from .serializers import ReceiptSerializer
import ipdb
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from works.models import Work


class ListCreateReceiptView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    def perform_create(self, serializer):
        work = get_object_or_404(Work, pk=self.kwargs["pk"])
        ipdb.set_trace()
        serializer.save(contractor=self.request.user, works=work)


class RetrieveUpdateDestroyReceiptView(RetrieveUpdateDestroyAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
