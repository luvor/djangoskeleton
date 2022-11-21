from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

import accounts.views as views

urlpatterns = [
    path("me/", views.UserProfileAPIView.as_view(), name="user-profile"),
    path("register/", views.UserCreateView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
