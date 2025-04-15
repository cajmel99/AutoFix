from rest_framework import viewsets, permissions
from .models import Service
from .serializers import ServiceSerializer
from users.permissions import IsMechanic


class MechanicServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated, IsMechanic]

    def get_queryset(self):
        return Service.objects.filter(mechanic=self.request.user.mechanic_profile)

    def perform_create(self, serializer):
        serializer.save(mechanic=self.request.user.mechanic_profile)


class PublicServiceListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Service.objects.all()
        mechanic_id = self.request.query_params.get('mechanic_id')
        city = self.request.query_params.get('city')

        if mechanic_id:
            queryset = queryset.filter(mechanic_id=mechanic_id)

        if city:
            queryset = queryset.filter(mechanic__city__icontains=city)

        return queryset

