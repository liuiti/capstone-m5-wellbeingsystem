from rest_framework import serializers
from .models import Avaliation


class AvaliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliation
        fields = "__all__"
