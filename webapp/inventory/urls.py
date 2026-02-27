from django.urls import path

from . import views

app_name = "inventory"

urlpatterns = [
    path("", views.product_list, name="product_list"),

    # products
    path("products/", views.product_list, name="product_list"),
    path("products/new/", views.product_create, name="product_create"),
    path("products/<int:pk>/edit/", views.product_update, name="product_update"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),

    # customers
    path("customers/register/", views.customer_register, name="customer_register"),

    # orders
    path("orders/new/", views.create_order, name="create_order"),
    path("orders/history/", views.order_history, name="order_history"),
]