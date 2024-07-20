import os
from pathlib import Path
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.conf import settings

from .models import Image
from .serializers import ImageSerializer

""" class ProductImages(APIView):
    
    def get(self, request, pk):
        data = Image.objects.all()
        serializer = ImageSerializer(data, many=True)
        return Response(serializer.data)
 """

class ImageView(APIView):

    def get(self, request, pk):
        data = Image.objects.get(id=pk)
        with open((settings.BASE_DIR / 'media' / Path(str(data.image_file))), 'rb') as f: 
            image_data = f.read()
        return HttpResponse(image_data, content_type='image/png')


class ImageViewName(APIView):

    def get(self, request, pk):
        idd = "product_images/" + pk
        print(idd)
        data = Image.objects.get(image_file=idd)
        
        with open(
            (settings.BASE_DIR / "media" / Path(str(data.image_file))), "rb"
        ) as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type="image/png")


class ImageThumbViewName(APIView):

    def get(self, request, pk):
        idd = "product_images/thumbnails/" + pk
        print(idd)
        data = Image.objects.get(thumbnail=idd)
        with open(
            (settings.BASE_DIR / "media" / Path(str(data.thumbnail))), "rb"
        ) as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type="image/png")


class ProfileImageViewName(APIView):

    def get(self, request, pk):
        idd = "profiles/" + pk
        print(idd)
        with open(
            (settings.BASE_DIR / "media" / idd), "rb"
        ) as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type="image/png")
