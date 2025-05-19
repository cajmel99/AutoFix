from django.db import models
from users.models import User


class Mechanic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mechanic_profile')
    name = models.CharField(max_length=255)  # workshop name
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.city})'
