from datetime import datetime
from django.db.models import Q
from autofix.const import TIME_BLOCK
from reservations.models import WorkingHours, Appointment


def get_available_timeslots(service, appointment_date):
    mechanic = service.mechanic
    day_of_week = appointment_date.strftime("%A").lower()
    working_hours = WorkingHours.objects.filter(
        mechanic=mechanic, day_of_the_week=day_of_week
    ).first()

    if not working_hours:
        return []

    appointments = Appointment.objects.filter(
        Q(service__mechanic=mechanic)
        & Q(date__day=appointment_date.day)
        & Q(date__month=appointment_date.month)
        & Q(date__year=appointment_date.year)
        & (Q(status="confirmed") | Q(status="pending"))
    )

    current_time = datetime.combine(appointment_date, working_hours.open_time)
    close_time = datetime.combine(appointment_date, working_hours.close_time)
    available_slots = []
    while current_time < close_time:
        potential_new_appointment_end_time = current_time + service.duration

        conflict = False
        for appointment in appointments:
            appointment_start_time = appointment.date.replace(tzinfo=None)
            appointment_end_time = appointment_start_time + appointment.service.duration
            appointment_end_time = appointment_end_time.replace(tzinfo=None)
            if not (
                current_time >= appointment_end_time
                or potential_new_appointment_end_time <= appointment_start_time
            ):
                conflict = True
                break
        if not conflict:
            available_slots.append(current_time)
        current_time += TIME_BLOCK
    return available_slots
