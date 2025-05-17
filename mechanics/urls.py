from django.urls import path
from .views import MechanicProfileView, MechanicListView

urlpatterns = [
    path('me/', MechanicProfileView.as_view(), name='mechanic-profile'),
    path('list/', MechanicListView.as_view(), name='mechanic-list')
]
