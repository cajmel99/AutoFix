from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta
from autofix.const import TIME_BLOCK
from mechanics.models import Mechanic


class Service(models.Model):
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.DurationField()  # np. "00:30:00" = 30 minut

    def clean(self):
        duration_minutes = self.duration.total_seconds() / 60
        time_block_minutes = TIME_BLOCK.total_seconds() / 60
        if duration_minutes % time_block_minutes != 0:
            raise ValidationError(f"Duration must be a multiple of {TIME_BLOCK}.")

    def __str__(self):
        return f"{self.name} - {self.mechanic.name}"

    def save(self, *args, **kwargs):
        self.clean()
        super(Service, self).save(*args, **kwargs)
