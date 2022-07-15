from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from accounts.models import Account
from .models import Receipt
from .serializers import PayedSerializer, ReceiptSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from works.models import Work
from accounts.permissions import IsSuperuserOrReadOnly
from .permission import IsConstractorPermission
from rest_framework import generics


class CreateReceiptView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    def perform_create(self, serializer):
        work = get_object_or_404(Work, pk=self.kwargs["pk"])
        serializer.save(contractor=self.request.user, works=work)


class RetrieveUpdateReceiptView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperuserOrReadOnly, IsConstractorPermission]

    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer


class UpdatePayed(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsConstractorPermission]

    queryset = Receipt.objects.all()
    serializer_class = PayedSerializer


class ListUsersFromReceipts(APIView):
    def get(self, request, pk):

        if Receipt.objects.all().filter(contractor=pk):
            receipts = Receipt.objects.all().filter(contractor=pk)
            serializer = ReceiptSerializer(receipts, many=True)

            return Response(serializer.data, status.HTTP_200_OK)

        user = Account.objects.get(pk=pk)
        works = Work.objects.all().filter(employee=user)
        for work in works:
            if len(Receipt.objects.all().filter(works=work)) == 0:
                break
            receipts = Receipt.objects.all().filter(works=work)

        serializer = ReceiptSerializer(receipts, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
