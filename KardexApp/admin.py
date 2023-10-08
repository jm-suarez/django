from django.contrib import admin
from .models import Producto, Saldo, Entrega, Ingreso


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass


@admin.register(Saldo)
class SaldoAdmin(admin.ModelAdmin):
    pass


@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    pass
