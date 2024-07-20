from django.urls import path

from .views import ImageView, ImageViewName, ProfileImageViewName, ImageThumbViewName
from accounts.views import GetProfileImg

urlpatterns = [
    #path('product/<str:pk>', ProductImages.as_view()),
    path('<int:pk>/', ImageView.as_view()),
    path('product_images/<str:pk>/', ImageViewName.as_view()),
    path('product_images/thumbnails/<str:pk>/', ImageThumbViewName.as_view()),
    path('profiles/<str:pk>/', ProfileImageViewName.as_view())
]
