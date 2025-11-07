import uuid
import bcrypt
from django.db import models

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)   # Store bcrypt hash created by NodeJS
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # If the password looks like raw text (not bcrypt hashed)
        if not self.password.startswith("$2b$"):
            # Hash using bcrypt
            self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
