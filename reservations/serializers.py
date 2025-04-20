from rest_framework import serializers
from django.utils.timezone import make_aware
from reservations.models import WorkingHours, Appointment
from reservations.utils import get_available_timeslots


class WorkingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingHours
        fields = ["id", "day_of_the_week", "open_time", "close_time"]


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["id", "client_user", "service", "date", "status"]
        read_only_fields = ["id", "client_user", "status"]

    def validate(self, attrs):
        service = attrs.get("service")
        date = attrs.get("date")

        if not service or not date:
            return attrs

        # if date.tzinfo is None:
        #     date = make_aware(date)

        available_slots = get_available_timeslots(service, date.date())
        date = date.replace(tzinfo=None)
        if date not in available_slots:
            raise serializers.ValidationError("This timeslot is not available.")

        return attrs
