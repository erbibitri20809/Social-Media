from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('post/', views.post_form, name='post_view'),

]