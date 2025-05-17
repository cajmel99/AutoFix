from rest_framework import generics, permissions
from .models import Mechanic
from .serializers import MechanicSerializer
from users.permissions import IsMechanic, IsClient


class MechanicProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = MechanicSerializer
    permission_classes = [permissions.IsAuthenticated, IsMechanic]

    def get_object(self):
        return self.request.user.mechanic_profile


class MechanicListView(generics.ListAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
    permission_classes = [permissions.AllowAny]
