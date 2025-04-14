from django.urls import path
from .views import MechanicProfileView

urlpatterns = [
    path('me/', MechanicProfileView.as_view(), name='mechanic-profile'),
]
