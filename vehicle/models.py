import uuid

from django.db import models

from account.models import User

class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.CharField(max_length=255)
    plate = models.CharField(max_length=7)
    year = models.IntegerField(null=True, blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plate

