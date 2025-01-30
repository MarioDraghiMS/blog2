# filepath: /c:/Users/mstajniak/Desktop/PythonBootcamp2/projekty/blog2/posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('post/<int:post_id>/', views.post_details, name='post_details'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),
]