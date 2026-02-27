from django import forms
from django.core.exceptions import ValidationError

from .models import Product, Customer


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "price", "quantity_in_stock"]

    def clean_quantity_in_stock(self):
        qty = self.cleaned_data["quantity_in_stock"]
        if qty < 0:
            raise ValidationError("Stock quantity cannot be negative.")
        return qty

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise ValidationError("Price cannot be negative.")
        return price


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "email"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email.endswith(".com") and not email.endswith(".ma"):
            raise ValidationError("Please use a .com or .ma email address.")
        return email


class OrderCreateForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField(min_value=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 👇 This controls how each object is shown in the dropdowns
        self.fields["customer"].label_from_instance = (
            lambda obj: f"{obj.name} ({obj.email})"
        )
        self.fields["product"].label_from_instance = (
            lambda obj: f"{obj.name} ({obj.category})"
        )

    def clean_quantity(self):
        qty = self.cleaned_data["quantity"]
        product = self.cleaned_data.get("product")
        if product and qty > product.quantity_in_stock:
            raise ValidationError(
                f"Not enough stock. Available: {product.quantity_in_stock}"
            )
        return qty