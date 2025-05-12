from django.db import models
import uuid
from users.models import User
from services.models import Service
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    review_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # unikalny identyfikator
    note = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    content = models.TextField(default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # data utworzenia
    updated_at = models.DateTimeField(auto_now=True)  # data aktualizacji
