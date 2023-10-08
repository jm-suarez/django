from datetime import date
from django import forms
from .models import Producto, Saldo, Entrega, Ingreso


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["descripcion"]

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")

        if not descripcion:
            raise forms.ValidationError("Este campo es requerido.")

        if len(descripcion) < 5:
            raise forms.ValidationError(
                "La descripción debe tener al menos 5 caracteres."
            )

        if len(descripcion) > 100:
            raise forms.ValidationError(
                "La descripción debe tener un maximo de 100 caracteres."
            )

        return descripcion


class SaldoForm(forms.ModelForm):
    class Meta:
        model = Saldo
        fields = ["codigo", "cantidad"]

    def clean(self):
        cleaned_data = super().clean()
        codigo = cleaned_data.get("codigo")
        cantidad = cleaned_data.get("cantidad")

        if not codigo:
            raise forms.ValidationError("El campo Código es requerido.")

        if cantidad < 0:
            raise forms.ValidationError("La cantidad debe ser mayor o igual a 0.")

        return cleaned_data


class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ["fecha", "codigo", "cantidad"]

    def clean(self):
        cleaned_data = super().clean()
        codigo = cleaned_data.get("codigo")
        fecha = cleaned_data.get("fecha")
        cantidad = cleaned_data.get("cantidad")

        if not codigo:
            raise forms.ValidationError("El campo Código es requerido.")

        if cantidad < 0:
            raise forms.ValidationError("La cantidad debe ser mayor o igual a 0.")

        if fecha is not None:
            if fecha > date.today():
                raise forms.ValidationError("La fecha no puede ser en el futuro.")

        return cleaned_data


class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ["fecha", "codigo", "cantidad"]

    def clean(self):
        cleaned_data = super().clean()
        codigo = cleaned_data.get("codigo")
        fecha = cleaned_data.get("fecha")
        cantidad = cleaned_data.get("cantidad")

        if not codigo:
            raise forms.ValidationError("El campo Código es requerido.")

        if cantidad < 0:
            raise forms.ValidationError("La cantidad debe ser mayor o igual a 0.")

        if fecha is not None:
            if fecha > date.today():
                raise forms.ValidationError("La fecha no puede ser en el futuro.")

        return cleaned_data
