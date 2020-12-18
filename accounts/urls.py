from django.urls import path

from .views.auth import UserLoginApiView

urlpatterns = [
    path('api/login/', UserLoginApiView.as_view(), name='api_login'),
]
