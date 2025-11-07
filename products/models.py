from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.IntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
