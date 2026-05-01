from django.contrib import admin
from .models import Buyer, Camera, CartItem

admin.site.register(Buyer)
admin.site.register(Camera)
admin.site.register(CartItem)