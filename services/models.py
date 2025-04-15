from django.db import models
from mechanics.models import Mechanic


class Service(models.Model):
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.DurationField()  # np. "00:30:00" = 30 minut

    def __str__(self):
        return f"{self.name} - {self.mechanic.name}"
