from django.shortcuts import render
from rest_framework import generics

from .models import Creditor, Debtor
from .serializers import CreditorSerializer, DebtorSerializer

# views = Endpoint


class CreditorView(generics.CreateAPIView):
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer


class DebtorView(generics.CreateAPIView):
    queryset = Debtor.objects.all()
    serializer_class = DebtorSerializer
