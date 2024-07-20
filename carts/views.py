from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated

from .models import CartItem
from .serializers import CartItemSerializer
from .permissions import IsOwner

from products.models import Product
from products.serializers import ProductSerializer


class CartList(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            # return CartItem.objects.filter(user=pk)
            return CartItem.objects.all()
        except CartItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        testData = CartItem.objects.all()
        print([x.product.name for x in testData])
        # data = self.get_object(request.user.id)
        data = self.get_object(3)
        serializer = CartItemSerializer(data, many=True)
        print()
        print([str(d["product"]) for d in serializer.data])
        if serializer.data:
            for dat in range(len(serializer.data)):
                serializer.data[dat]["product"] = ProductSerializer(
                    Product.objects.get(id=str(serializer.data[dat]["product"]))
                ).data
        print(serializer.data)
        return Response({"items": serializer.data})

    def post(self, request):
        print("in post:")
        print(request.data)
        print(request.user.id)
        serializer = CartItemSerializer(data={**request.data, "user": request.user.id})
        print(serializer.is_valid())
        if serializer.is_valid():
            print("valid")
            newCartItem = serializer.save()
        return Response(serializer.data)
    
    def delete(self, request):
        pass


class CheckUser(APIView):
    def get(self, request):
        print(request.user)
        return Response({"user": str(request.user)})


class CartItemView(APIView):

    def get_object(self, pk):
        try:
            return CartItem.objects.get(id=pk)
        except CartItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        data = self.get_object(pk)
        serializer = CartItemSerializer(data)
        return Response(serializer.data)

    def delete(self, request, pk):
        print(self.get_object(pk))
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_200_OK)
