from django.contrib import admin

from .models import CartItem


class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "quantity",
        "user",
        "date_added"
    )


admin.site.register(CartItem, CartItemAdmin)
