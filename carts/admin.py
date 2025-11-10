from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    list_filter = ('created_at',)

@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'created_at')
    list_filter = ('created_at',)
