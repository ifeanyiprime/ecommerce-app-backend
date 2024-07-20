from django.urls import path

from .views import CartList, CheckUser, CartItemView

urlpatterns = [
    path("", CartList.as_view()),
    path("user/", CheckUser.as_view()),
    path("<int:pk>/", CartItemView.as_view())
]
