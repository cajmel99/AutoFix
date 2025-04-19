import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autofix.settings")
django.setup()

from users.models import User
from users.serializers import RegisterSerializer
from mechanics.models import Mechanic
from services.models import Service
from datetime import timedelta

Service.objects.all().delete()
Mechanic.objects.all().delete()
User.objects.filter(is_superuser=False).delete()


users_data = [
    {
        "email": "client1@example.com",
        "password": "clientpass123",
        "name": "Anna",
        "surname": "Nowak",
        "phone": "123456789",
        "role": "client",
    },
    {
        "email": "mechanic1@example.com",
        "password": "mechanicpass123",
        "name": "Marek",
        "surname": "Kowalski",
        "phone": "987654321",
        "role": "mechanic",
    },
]

for user_data in users_data:
    serializer = RegisterSerializer(data=user_data)
    if serializer.is_valid():
        serializer.save()

mechanic_user = User.objects.get(email="mechanic1@example.com")
mechanic = Mechanic.objects.get(user=mechanic_user)

services_data = [
    {"name": "Wymiana oleju", "price": 150.00, "duration": timedelta(minutes=30)},
    {
        "name": "Diagnostyka komputerowa",
        "price": 100.00,
        "duration": timedelta(minutes=60),
    },
    {
        "name": "Wymiana klocków hamulcowych",
        "price": 200.00,
        "duration": timedelta(minutes=45),
    },
    {"name": "Serwis klimatyzacji", "price": 250.00, "duration": timedelta(hours=1)},
]
for service_data in services_data:
    service = Service.objects.create(mechanic=mechanic, **service_data)
