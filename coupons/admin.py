from django.contrib import admin
from .models import Coupon, UserCoupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'type', 'discount_percent', 'nth_value', 'is_active', 'created_at')
    list_filter = ('created_at',)

@admin.register(UserCoupon)
class UserCouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'coupon', 'order', 'used_at')
    list_filter = ('used_at',)
