from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import os
import mimetypes
from django.conf import settings
from django.http import HttpResponse


from .models import Product
from images.models import Image
from .serializers import ProductSerializer
from images.serializers import ImageSerializer

class ProductList(APIView):
    # queryset = Product.objects.all()
    # serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        product_data = Product.objects.all()
        product_serializer = ProductSerializer(product_data, many=True)
        for x in product_serializer.data:
            x["images"] = ImageSerializer(
                Image.objects.filter(product=x['id'], main=True),
                many=True,
            ).data
        print(product_serializer.data)
        return Response(product_serializer.data)


class ProductDetail(APIView):
    # queryset = Product.objects.all()
    # serializer_class = ProductSerializer

    def get(self, request, pk):
        product_data = Product.objects.get(pk=pk)
        image_data = Image.objects.filter(product=pk)
        product_serializer = ProductSerializer(product_data)
        image_serializer = ImageSerializer(image_data, many=True)
        product_serializer.data['images'] = image_serializer.data
        newP = {'images': image_serializer.data}
        print({**product_serializer.data, **newP})
        return Response({**product_serializer.data, **newP})

def test(request, pk):
    with open(
        os.path.join(settings.BASE_DIR, "static", "images", pk), "rb"
    ) as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type=mimetypes.guess_type(pk)[0])
