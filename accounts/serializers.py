from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "email",
            "name",
            "is_worker",
            "birth_date",
            "date_joined",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "birth_date": {
                "format": "%d/%m/%Y",
                "input_formats": ["%d-%m-%Y", "iso-8601"],
            },
        }

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(write_only=True)
