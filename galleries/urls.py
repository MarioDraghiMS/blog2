from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_list, name='gallery_list'),
    path('new/', views.gallery_create, name='gallery_create'),
    path('<int:gallery_id>/', views.gallery_detail, name='gallery_detail'),
    path('<int:gallery_id>/add_photo/', views.photo_add, name='photo_add'),
]