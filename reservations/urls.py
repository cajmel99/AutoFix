from django.urls import path
from reservations.views import (
    AppointmentCreateView,
    AppointmentCancelView,
    ClientAppointmentsListView,
    MechanicWorkingHoursView,
    MechanicAppointmentsListView,
    AppointmentStatusUpdateView,
    AvailableTimeslotsView,
    MechanicWorkingHoursDetailView,
)

urlpatterns = [
    # Client
    path(
        "client/appointments/",
        AppointmentCreateView.as_view(),
        name="create_appointment",
    ),
    path(
        "client/appointments/cancel/<int:pk>/",
        AppointmentCancelView.as_view(),
        name="cancel_appointment",
    ),
    path(
        "client/appointments/list/",
        ClientAppointmentsListView.as_view(),
        name="client_appointments",
    ),
    path(
        "client/available-timeslots/<int:service_id>/<str:appointment_date>/",
        AvailableTimeslotsView.as_view(),
        name="available_timeslots",
    ),
    # Mechanic
    path(
        "mechanic/working-hours/",
        MechanicWorkingHoursView.as_view(),
        name="mechanic_working_hours",
    ),
    path(
        "mechanic/working-hours/<int:pk>/",
        MechanicWorkingHoursDetailView.as_view(),
        name="mechanic_working_hours_detail",
    ),
    path(
        "mechanic/appointments/",
        MechanicAppointmentsListView.as_view(),
        name="mechanic_appointments",
    ),
    path(
        "mechanic/appointments/<int:pk>/update-status/",
        AppointmentStatusUpdateView.as_view(),
        name="update_appointment_status",
    ),
]
