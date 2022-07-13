from rest_framework import serializers
from .models import Work
from accounts.serializers import AccountSerializer
from categories.serializers import CategorySerializer
from categories.models import Category

class WorkSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    class Meta:
        model = Work
        fields = "__all__"

class ListWorksSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Work
        fields = "__all__"