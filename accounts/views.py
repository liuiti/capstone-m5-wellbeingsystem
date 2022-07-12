from rest_framework.views import APIView, Response, status
from rest_framework import generics

from accounts.permissions import IsSuperuserOrReadOnly, UserEqual
from .models import Account

from .serializers import AccountSerializer, LoginSerializer

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ListAccountView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CreateAccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class RetriveUpdateDeleteAccountView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserEqual | IsSuperuserOrReadOnly]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})

        return Response(
            {"detail": "invalid email or password"}, status.HTTP_401_UNAUTHORIZED
        )
