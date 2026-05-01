from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:camera_id>/', views.add_to_cart, name='add_to_cart'),
]