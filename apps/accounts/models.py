from django.contrib.auth.models import User
from django.db import models

from abstract_models.time_stamped_model import TimeStamped


class Account(TimeStamped):
    class Status(models.TextChoices):
        CUSTOMER = "CUSTOMER"
        SELLER = "SELLER"

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )
    status = models.CharField(
        max_length=21,
        choices=Status.choices,
        default=Status.CUSTOMER,
        verbose_name="Status",
    )

    def __str__(self):
        return f"{self.user.username}-{self.status}"
