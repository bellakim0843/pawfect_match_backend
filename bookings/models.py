from django.db import models
from common.models import CommonModel


# Create your models here.
class Booking(CommonModel):
    class BookingKindChoices(models.TextChoices):
        BOARDER = "boarder", "Boarder"
        SITTER = "sitter", "Sitter"

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    # boarder = models.ForeignKey(
    #     "boarders.Boarder",
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name="bookings",
    # )
    sitter = models.ForeignKey(
        "sitters.Sitter",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookings",
    )

    # daycare_day = models.DateField(
    #     null=True,
    #     blank=True,
    # )

    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )

    pets = models.PositiveIntegerField(
        default=1,
    )

    def __str__(self) -> str:
        return f"{self.kind.title()} Booking for: {self.user}"
