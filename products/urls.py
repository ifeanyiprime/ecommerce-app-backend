from django.urls import path

from .views import ProductList, ProductDetail, test

urlpatterns = [
    path("media/profiles/<str:pk>/", test),
    path("<str:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("", ProductList.as_view(), name="product_list"),
]