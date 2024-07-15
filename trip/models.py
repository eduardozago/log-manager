import uuid

from django.db import models

from vehicle.models import Vehicle
from branch.models import Branch

class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    origin = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='trip_origin')
    destiny = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='trip_destiny')

    date_joined = models.DateTimeField(auto_now_add=True)

    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.vehicle.name} from {self.origin} to {self.destiny}'
