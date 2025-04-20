from django.db import models
from users.models import User
from mechanics.models import Mechanic
from services.models import Service

# Create your models here.


class Appointment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
    ]

    client_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="appointments"
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="appointments"
    )
    date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.client_user.email} - {self.service.name} on {self.date.strftime('%Y-%m-%d %H:%M')}"


class WorkingHours(models.Model):
    DAYS_OF_WEEK = [
        ("monday", "Monday"),
        ("tuesday", "Tuesday"),
        ("wednesday", "Wednesday"),
        ("thursday", "Thursday"),
        ("friday", "Friday"),
        ("saturday", "Saturday"),
        ("sunday", "Sunday"),
    ]

    mechanic = models.ForeignKey(
        Mechanic, on_delete=models.CASCADE, related_name="working_hours"
    )
    day_of_the_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        unique_together = ("mechanic", "day_of_the_week")
        ordering = ["mechanic", "day_of_the_week"]

    def __str__(self):
        return f"{self.mechanic.user.email} - {self.day_of_the_week.capitalize()} {self.open_time}–{self.close_time}"
