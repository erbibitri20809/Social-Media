from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.custom_logout, name='logout')
]