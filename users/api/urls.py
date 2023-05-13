from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]