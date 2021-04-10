from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from server.serializers import *
from knox.models import AuthToken
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django_filters.rest_framework import DjangoFilterBackend
from server.filter import *
from server.models import *

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    parser_classes = [MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProduceFilter

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class BigmarketViewSet(viewsets.ModelViewSet):
    queryset = Bigmarket.objects.all()
    serializer_class = BigmarketSerializer

