from rest_framework import generics, permissions
from .models import Mechanic
from .serializers import MechanicSerializer
from users.permissions import IsMechanic


class MechanicProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = MechanicSerializer
    permission_classes = [permissions.IsAuthenticated, IsMechanic]

    def get_object(self):
        return self.request.user.mechanic_profile
