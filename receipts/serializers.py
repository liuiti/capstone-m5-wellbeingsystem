from rest_framework import serializers
from works.serializers import ListWorksSerializer
from accounts.serializers import AccountSerializer
from .models import Receipt


class ReceiptSerializer(serializers.ModelSerializer):
    works = ListWorksSerializer(read_only=True)
    contractor = AccountSerializer(read_only=True)

    class Meta:
        model = Receipt
        exclude = ["payed"]


class PayedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = "__all__"

    def update(self, instance: Receipt, validated_data):

        if validated_data["payed"] == False:
            raise serializers.ValidationError(
                {"payed": "Não pode alterar o valor de 'payed' para False"}
            )

        instance.payed = validated_data.get("payed", instance.payed)
        return instance
