from django.contrib import admin
from reservations.models import Appointment, WorkingHours

# Register your models here.

admin.site.register(Appointment)
admin.site.register(WorkingHours)
