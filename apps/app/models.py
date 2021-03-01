from django.db import models

from apps.utils.models import Timestamps
from apps.authentication.models import User


class Trip(Timestamps):
    trip_id = models.CharField(max_length=100)
    pickup_address = models.TextField()
    destination_address = models.TextField()
    purpose = models.TextField()

    provider_id = models.IntegerField()
    provider_name = models.CharField(max_length=200)
    provider_phone_number = models.CharField(max_length=20)

    create_time = models.CharField(max_length=50)
    completed_time = models.CharField(max_length=50)

    amount = models.FloatField()
    approval_status = (
        (1, 'Pending'),
        (2, 'Approved'),
        (3, 'Rejected'),
    )
    status = models.IntegerField(choices=approval_status, default=1)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
