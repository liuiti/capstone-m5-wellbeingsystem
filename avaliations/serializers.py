from rest_framework import serializers

from receipts.serializers import ReceiptSerializer
from .models import Avaliation


class AvaliationSerializer(serializers.ModelSerializer):
    receipt = ReceiptSerializer(read_only=True)

    class Meta:
        model = Avaliation
        fields = "__all__"

    def create(self, validated_data):

        if validated_data["stars"] > 10:
            raise serializers.ValidationError(
                {"stars": ["Ensure this value is less than or equal to 10."]}
            )

        if validated_data["stars"] < 1:
            raise serializers.ValidationError(
                {"stars": ["Ensure this value is greater than or equal to 1."]}
            )

        avaliation = Avaliation.objects.create(**validated_data)

        return avaliation
