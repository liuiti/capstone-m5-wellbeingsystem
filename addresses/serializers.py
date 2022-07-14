from rest_framework import serializers
from .models import Address
from accounts.serializers import AccountSerializer


class AddressSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    class Meta:
        model = Address
        fields = "__all__"