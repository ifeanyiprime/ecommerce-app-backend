from django.urls import path, include
from .views import AccountList, AccountDetail, GetProfileImg


urlpatterns = [
    path("", AccountList.as_view()),
    path("user/", AccountDetail.as_view()),
    path("profile/", GetProfileImg.as_view()),
]
