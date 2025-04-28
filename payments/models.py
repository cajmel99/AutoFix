from django.db import models
import uuid
from users.models import User

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    PAYMENT_METHODS = [
        ('blik', 'BLIK'),
        ('cash', 'Cash'),
        ('card', 'Card'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # unikalny identyfikator
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)  # data utworzenia
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHODS, default='cash')