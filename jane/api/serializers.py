# Takes the model and converts it into JSON format
from rest_framework import serializers

from .models import Creditor, Debtor


class CreditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creditor
        fields = "__all__"


class DebtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debtor
        fields = "__all__"
