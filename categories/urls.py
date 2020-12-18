from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.all_categories, name='categories'),
    # path('create_category/', views.create_category, name='create_category'),
]