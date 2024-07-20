import os

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse

from .models import CustomUser
from .serializers import CustomUserSerializer
from django.conf import settings

class AccountList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class AccountDetail(APIView):
    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response({'user' : serializer.data})
    

class GetProfileImg(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        image_link = CustomUser.objects.get(request.user.id).profile_img
        with open(os.path.join(settings.BASE_DIR, 'media', str(image_link)), 'rb') as f:
            image_data = f.read()
        print(settings.BASE_DIR)
        return HttpResponse(image_data, content_type='image/png')
    