from rest_framework import serializers

from .models import CartItem
from products.models import Product
from accounts.models import CustomUser


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            "id",
            "product",
            "user",
            "quantity",
            "date_added",
        )
    
    def create(self, validated_data):
        print(validated_data)
        cartItem = CartItem.objects.create(
            product = validated_data['product'],
            user = validated_data['user'],
            quantity = validated_data['quantity']
        )
        cartItem.save()
        return cartItem
