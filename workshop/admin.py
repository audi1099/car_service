from django.contrib import admin
from .models import Client, Car, RepairOrder

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "email")
    search_fields = ("first_name", "last_name", "phone", "email")

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "year", "owner")
    search_fields = ("brand", "model", "vin")
    list_filter = ("year",)

@admin.register(RepairOrder)
class RepairOrderAdmin(admin.ModelAdmin):
    list_display = ("car", "status", "created_at")
    search_fields = ("car__brand", "car__model")
    list_filter = ("status", "created_at")
    ordering = ("-created_at",)