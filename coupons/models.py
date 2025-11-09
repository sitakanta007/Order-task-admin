import uuid
from django.db import models
from customers.models import Customer
from orders.models import Order

class Coupon(models.Model):
    COUPON_TYPES = (
        ('percentage', 'Percentage'),
        ('flat_rate', 'Flat Rate'),
        ('hybrid', 'Hybrid'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=20, choices=COUPON_TYPES)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    flat_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    nth_value = models.IntegerField()                  # per-user order cadence
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} ({self.type})"


class UserCoupon(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    used_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_id', 'coupon')

    def __str__(self):
        return f"{self.user_id} used {self.coupon.code}"
