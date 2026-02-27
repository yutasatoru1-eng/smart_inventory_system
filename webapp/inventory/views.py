from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone

from .models import Product, Customer, Order, OrderItem
from .forms import ProductForm, CustomerForm, OrderCreateForm


# ---------- PRODUCTS ----------

def product_list(request):
    products = Product.objects.all().order_by("name")
    return render(request, "inventory/product_list.html", {"products": products})


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully.")
            return redirect("inventory:product_list")
    else:
        form = ProductForm()

    return render(request, "inventory/product_form.html", {"form": form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            return redirect("inventory:product_list")
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        "inventory/product_form.html",
        {"form": form, "product": product},
    )


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted.")
        return redirect("inventory:product_list")

    return render(
        request,
        "inventory/product_confirm_delete.html",
        {"product": product},
    )


# ---------- CUSTOMERS ----------

def customer_register(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer registered successfully.")
            return redirect("inventory:product_list")
    else:
        form = CustomerForm()

    return render(request, "inventory/customer_register.html", {"form": form})


# ---------- ORDERS ----------

def create_order(request):
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data["customer"]
            product = form.cleaned_data["product"]
            quantity = form.cleaned_data["quantity"]

            # 1) order
            order = Order.objects.create(
                customer=customer,
                order_date=timezone.now(),
            )

            # 2) item
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                unit_price=product.price,
            )

            # 3) update stock
            product.quantity_in_stock -= quantity
            product.save()

            messages.success(request, f"Order #{order.id} created successfully.")
            return redirect("inventory:order_history")
    else:
        form = OrderCreateForm()

    return render(request, "inventory/order_form.html", {"form": form})


def order_history(request):
    orders = (
        Order.objects
        .select_related("customer")
        .prefetch_related("items__product")
        .order_by("-order_date")
    )

    order_data = []
    for order in orders:
        total = sum(item.quantity * item.unit_price for item in order.items.all())
        order_data.append({"order": order, "total": total})

    return render(request, "inventory/order_history.html", {"orders": order_data})
