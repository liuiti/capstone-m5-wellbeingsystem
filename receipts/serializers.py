from rest_framework import serializers
import ipdb
from works.serializers import ListWorksSerializer
from accounts.serializers import AccountSerializer
from .models import Receipt


class ReceiptSerializer(serializers.ModelSerializer):
    works = ListWorksSerializer(read_only=True)
    contractor = AccountSerializer(read_only=True)

    class Meta:
        model = Receipt
        fields = "__all__"
        # fields = [
        #     "id",
        #     "works",
        #     "price",
        #     "contractor",
        #     "input_date",
        #     "output_date",
        # ]
