from rest_framework import serializers
from server.models import *
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'location', 'desc', 'mainpic', 'categ', 'period', 'hour', 'website', 'pic1', 'pic2', 'pic3', 'clap')
        extra_kwargs = {'id': {'validators': []}}


class LoginSerializer(serializers.ModelSerializer):
#    store = StoreSerializer(many=True, required=False)
    class Meta:
        model = Login
        fields = ('id', 'pw', 'email', 'nickname')
        extra_kwargs = {'id': {'validators': []}}

class BigmarketSerializer(serializers.ModelSerializer):
#    store = StoreSerializer(many=True, required=False)
    class Meta:
        model = Bigmarket
        fields = ('id', 'name', 'location', 'pic', 'store')
        extra_kwargs = {'id': {'validators': []}}
