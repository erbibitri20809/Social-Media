from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.home_view, name='home_view'),
    path('post/', views.post_form, name='post_view'),
    path('profile/', views.profile_view, name='profile_view'),
    path('open/<int:id>/', views.open_view, name='open_view'),
    path('delete/<int:id>/', views.delete_picture, name='delete_picture'),
    path('comment/<int:id>/', views.add_comment, name='add_comment'),
    path('update/<int:id>/', views.update_desc, name='update_desc'),
    path('post_story/', views.story_form, name='story_form'),
    path('story_view/<int:pk>/', views.story_view, name='story_view'),

]