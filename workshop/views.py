from rest_framework import viewsets
from .serializers import ClientSerializer, CarSerializer, RepairOrderSerializer
from django.shortcuts import render
from .models import Client, Car, RepairOrder

def home(request):
    clients = Client.objects.all()
    cars = Car.objects.all()
    orders = RepairOrder.objects.all()
    return render(request, 'index.html', {
        'clients': clients,
        'cars': cars,
        'orders': orders,
    })

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class RepairOrderViewSet(viewsets.ModelViewSet):
    queryset = RepairOrder.objects.all()
    serializer_class = RepairOrderSerializer
