from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from server.serializers import *


class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class BigmarketViewSet(viewsets.ModelViewSet):
    queryset = Bigmarket.objects.all()
    serializer_class = BigmarketSerializer
