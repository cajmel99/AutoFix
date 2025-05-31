from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from reservations.models import WorkingHours, Appointment, Mechanic
from reservations.serializers import WorkingHoursSerializer, AppointmentSerializer
from reservations.utils import get_available_timeslots
from users.permissions import IsMechanic, IsClient
from django.http import JsonResponse
from datetime import datetime
from services.models import Service


# Create your views here.


# Client endpoints
class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsClient]

    def perform_create(self, serializer):
        serializer.save(client_user=self.request.user)


class AppointmentCancelView(generics.UpdateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsClient]

    def get_queryset(self):
        return Appointment.objects.filter(
            client_user=self.request.user, status="pending"
        )

    def perform_update(self, serializer):
        serializer.save(status="cancelled")


class ClientAppointmentsListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsClient]

    def get_queryset(self):
        return Appointment.objects.filter(client_user=self.request.user)


class ClientCheckWorkingHoursView(generics.ListAPIView):
    serializer_class = WorkingHoursSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        mechanic_id = self.kwargs.get("mechanic_id")
        if not Mechanic.objects.filter(id=mechanic_id).exists():
            raise NotFound("Mechanic not found.")
        return WorkingHours.objects.filter(mechanic_id=mechanic_id)


# Mechanic endpoints
class MechanicWorkingHoursView(generics.ListCreateAPIView):
    serializer_class = WorkingHoursSerializer
    permission_classes = [permissions.IsAuthenticated, IsMechanic]

    def get_queryset(self):
        mechanic = Mechanic.objects.get(user=self.request.user)
        return WorkingHours.objects.filter(mechanic=mechanic)

    def perform_create(self, serializer):
        mechanic = Mechanic.objects.get(user=self.request.user)
        serializer.save(mechanic=mechanic)


class MechanicWorkingHoursDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkingHoursSerializer
    permission_classes = [permissions.IsAuthenticated, IsMechanic]

    def get_queryset(self):
        mechanic = Mechanic.objects.get(user=self.request.user)
        return WorkingHours.objects.filter(mechanic=mechanic)

    def perform_update(self, serializer):
        mechanic = Mechanic.objects.get(user=self.request.user)

        serializer.save(mechanic=mechanic)


class MechanicAppointmentsListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsMechanic]

    def get_queryset(self):
        return Appointment.objects.filter(service__mechanic__user=self.request.user)


class AppointmentStatusUpdateView(generics.UpdateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsMechanic]

    def get_queryset(self):
        return Appointment.objects.filter(service__mechanic__user=self.request.user)

    def patch(self, request, *args, **kwargs):
        appointment = self.get_object()
        new_status = request.data.get("status")

        if new_status not in ["confirmed", "cancelled", "completed"]:
            return Response(
                {"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST
            )

        appointment.status = new_status
        appointment.save()
        return Response(AppointmentSerializer(appointment).data)


class AvailableTimeslotsView(APIView):
    def get(self, request, service_id, appointment_date):
        try:
            appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d")
        except ValueError:
            return JsonResponse(
                {"error": "Invalid date format. Use YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            service = Service.objects.get(id=service_id)
        except Service.DoesNotExist:
            return JsonResponse(
                {"error": "Service not found."}, status=status.HTTP_404_NOT_FOUND
            )

        available_slots = get_available_timeslots(service, appointment_date)

        if available_slots:
            return Response(
                {"available_slots": available_slots}, status=status.HTTP_200_OK
            )
        else:
            return JsonResponse(
                {"message": "No available slots."}, status=status.HTTP_404_NOT_FOUND
            )
