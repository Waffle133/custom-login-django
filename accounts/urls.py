from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('test/', views.test, name='test'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('create_permission/', views.create_permission, name='create_permission'),
    path('remove_permission/', views.remove_permission, name='remove_permission'),
]
