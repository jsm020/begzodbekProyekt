from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from .models import Mahsulotlar, Mahsulot_rasm
from rest_framework.decorators import action


class MahsulotRasmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot_rasm
        fields = ('id', 'image')

class MahsulotlarSerializer(serializers.ModelSerializer):
    images = MahsulotRasmSerializer(many=True, read_only=True)

    class Meta:
        model = Mahsulotlar
        fields = ('id', 'category', 'name', 'title', 'price', 'oldprice', 'discount', 'images')

