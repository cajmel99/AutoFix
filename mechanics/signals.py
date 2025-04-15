from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from .models import Mechanic


@receiver(post_save, sender=User)
def create_mechanic_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'mechanic':
        Mechanic.objects.create(
            user=instance,
            name=f"Warsztat {instance.name}",
            address="Adres nieuzupełniony",
            city="Miasto nieuzupełnione"
        )
