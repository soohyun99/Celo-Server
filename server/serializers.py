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


#class LoginSerializer(WritableNestedModelSerializer):
#    store = StoreSerializer(many=True, required=False)
#    class Meta:
#        model = Login
#        fields = ('id', 'pw', 'email', 'nickname', 'store')
#        extra_kwargs = {'id': {'validators': []}}

class BigmarketSerializer(WritableNestedModelSerializer):
    store = StoreSerializer(many=True, required=False)
    class Meta:
        model = Bigmarket
        fields = ('id', 'name', 'location', 'pic', 'store')
        extra_kwargs = {'id': {'validators': []}}

# 회원가입 시리얼라이저

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user


# 접속 유지중인지 확인할 시리얼라이저

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


# 로그인 시리얼라이저

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")