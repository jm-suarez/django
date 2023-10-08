from django.shortcuts import redirect
from django.views.generic import ListView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Producto, Entrega, Ingreso, Saldo
from .forms import ProductoForm, SaldoForm, EntregaForm, IngresoForm
from .serializers import (
    ProductoSerializer,
    SaldoSerializer,
    EntregaSerializer,
    IngresoSerializer,
)


class ProductoListApi(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)


class ProductoListView(ListView):
    model = Producto
    template_name = "productos.html"


@require_http_methods(["POST"])
def producto_store(request):
    form = ProductoForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Producto creado satisfactoriamente")
    else:
        error_messages = [
            f"{field}: {', '.join(errors)}" for field, errors in form.errors.items()
        ]
        for error_message in error_messages:
            messages.error(request, error_message)
    return redirect("producto-list")


@require_http_methods(["POST"])
def producto_update(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    form = ProductoForm(request.POST, instance=producto)
    if form.is_valid():
        form.save()
        messages.success(request, "Producto actualizado satisfactoriamente")
    else:
        error_messages = [
            f"{field}: {', '.join(errors)}" for field, errors in form.errors.items()
        ]
        for error_message in error_messages:
            messages.error(request, error_message)
    return redirect("producto-list")


@require_http_methods(["DELETE"])
def producto_delete(request, producto_id):
    try:
        producto = get_object_or_404(Producto, pk=producto_id)
        producto.delete()
        return JsonResponse({"message": "Producto eliminado satisfactoriamente"})
    except Producto.DoesNotExist:
        return JsonResponse({"error": "El producto no existe"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def obtener_producto_por_id(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    data = {"codigo": producto.codigo, "descripcion": producto.descripcion}
    return JsonResponse(data)


class EntregaListApi(APIView):
    def get(self, request):
        entregas = Entrega.objects.all()
        serializer = EntregaSerializer(entregas, many=True)
        return Response(serializer.data)


class EntregaListView(ListView):
    model = Entrega
    template_name = "entregas.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productos"] = Producto.objects.all()
        return context


@require_http_methods(["POST"])
def entrega_store(request):
    form = EntregaForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Entrega creada satisfactoriamente")
    else:
        error_messages = [
            f"{field}: {', '.join(errors)}" for field, errors in form.errors.items()
        ]
        for error_message in error_messages:
            messages.error(request, error_message)
    return redirect("entrega-list")


@require_http_methods(["POST"])
def entrega_update(request, entrega_id):
    entrega = get_object_or_404(Entrega, pk=entrega_id)
    form = EntregaForm(request.POST, instance=entrega)
    if form.is_valid():
        form.save()
        messages.success(request, "Entrega actualizada satisfactoriamente")
    else:
        error_messages = [
            f"{field}: {', '.join(errors)}" for field, errors in form.errors.items()
        ]
        for error_message in error_messages:
            messages.error(request, error_message)
    return redirect("entrega-list")


@require_http_methods(["DELETE"])
def entrega_delete(request, entrega_id):
    try:
        entrega = get_object_or_404(Entrega, pk=entrega_id)
        entrega.delete()
        return JsonResponse({"message": "Entrega eliminada satisfactoriamente"})
    except Producto.DoesNotExist:
        return JsonResponse({"error": "El saldo no existe"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def obtener_entrega_por_id(request, entrega_id):
    entrega = get_object_or_404(Entrega, pk=entrega_id)
    data = {
        "id": entrega.id,
        "codigo": entrega.codigo.codigo,
        "fecha": entrega.fecha,
        "cantidad": entrega.cantidad,
    }
    return JsonResponse(data)


class IngresoListApi(APIView):
    def get(self, request):
        ingresos = Ingreso.objects.all()
        serializer = IngresoSerializer(ingresos, many=True)
        return Response(serializer.data)


class IngresoListView(ListView):
    model = Ingreso
    template_name = "ingresos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productos"] = Producto.objects.all()
        return context


@require_http_methods(["POST"])
def ingreso_store(request):
    form = IngresoForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Ingreso creado satisfactoriamente")
    else:
        error_messages = [
            f"{field}: {', '.join(errors)}" for field, errors in form.errors.items()
        ]
        for error_message in error_messages:
            messages.error(request, error_message)
    return redirect("ingreso-list")


@require_http_methods(["POST"])
def ingreso_update(request, ingreso_id):
    ingreso = get_object_or_404(Ingreso, pk=ingreso_id)
    form = IngresoForm(request.POST, instance=ingreso)
    if form.is_valid():
        form.save()
        messages.success(request, "Ingreso actualizado satisfactoriamente")
    else:
        error_messages = [
            f"{field}: {', '.join(errors)}" for field, errors in form.errors.items()
        ]
        for error_message in error_messages:
            messages.error(request, error_message)
    return redirect("ingreso-list")


@require_http_methods(["DELETE"])
def ingreso_delete(request, ingreso_id):
    try:
        ingreso = get_object_or_404(Ingreso, pk=ingreso_id)
        ingreso.delete()
        return JsonResponse({"message": "Ingreso eliminada satisfactoriamente"})
    except Producto.DoesNotExist:
        return JsonResponse({"error": "El saldo no existe"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def obtener_ingreso_por_id(request, ingreso_id):
    ingreso = get_object_or_404(Ingreso, pk=ingreso_id)
    data = {
        "id": ingreso.id,
        "codigo": ingreso.codigo.codigo,
        "fecha": ingreso.fecha,
        "cantidad": ingreso.cantidad,
    }
    return JsonResponse(data)


class SaldoListApi(APIView):
    def get(self, request):
        saldos = Saldo.objects.all()
        serializer = SaldoSerializer(saldos, many=True)
        return Response(serializer.data)


class SaldoListView(ListView):
    model = Saldo
    template_name = "saldos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productos"] = Producto.objects.all()
        return context


@require_http_methods(["POST"])
def saldo_store(request):
    form = SaldoForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Saldo creado satisfactoriamente")
    else:
        error_messages = [
            f"{field}: {', '.join(errors)}" for field, errors in form.errors.items()
        ]
        for error_message in error_messages:
            messages.error(request, error_message)
    return redirect("saldo-list")


@require_http_methods(["POST"])
def saldo_update(request, saldo_id):
    saldo = get_object_or_404(Saldo, pk=saldo_id)
    form = SaldoForm(request.POST, instance=saldo)
    if form.is_valid():
        form.save()
        messages.success(request, "Saldo actualizado satisfactoriamente")
    else:
        error_messages = [
            f"{field}: {', '.join(errors)}" for field, errors in form.errors.items()
        ]
        for error_message in error_messages:
            messages.error(request, error_message)
    return redirect("saldo-list")


@require_http_methods(["DELETE"])
def saldo_delete(request, saldo_id):
    try:
        saldo = get_object_or_404(Saldo, pk=saldo_id)
        saldo.delete()
        return JsonResponse({"message": "Saldo eliminado satisfactoriamente"})
    except Producto.DoesNotExist:
        return JsonResponse({"error": "El saldo no existe"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def obtener_saldo_por_id(request, saldo_id):
    saldo = get_object_or_404(Saldo, pk=saldo_id)
    data = {
        "id": saldo.id,
        "codigo": saldo.codigo.codigo,
        "cantidad": saldo.cantidad,
    }
    return JsonResponse(data)
