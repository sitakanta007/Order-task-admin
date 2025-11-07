from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'available_quantity')
    search_fields = ('title',)
    list_filter = ('price',)
