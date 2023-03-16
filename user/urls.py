from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import CustomTokenObtainPairView
from . import views

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('info/', views.UserInfoView.as_view(), name = 'user_info'),

]