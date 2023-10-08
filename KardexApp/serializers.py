# serializers.py
from rest_framework import serializers
from .models import Producto, Saldo, Entrega, Ingreso


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"


class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saldo
        fields = "__all__"


class EntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrega
        fields = "__all__"


class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = "__all__"
