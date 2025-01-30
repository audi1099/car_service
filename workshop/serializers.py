from rest_framework import serializers
from .models import Client, Car, RepairOrder

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'phone', 'email']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'owner', 'brand', 'model', 'year', 'vin']

class RepairOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairOrder
        fields = ['id', 'car', 'description', 'status', 'created_at']