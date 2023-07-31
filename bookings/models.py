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
        default=1,
    )

    sitter = models.ForeignKey(
        "sitters.Sitter",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookings",
    )

    owner = models.ForeignKey(
        "owners.Owner",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookings",
    )

    pet = models.ForeignKey(
        "owners.Pet",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookings",
    )

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

    # pet = models.ForeignKey(
    #     "users.Pet", on_delete=models.SET_NULL, null=True, blank=True
    # )

    def __str__(self) -> str:
        return f"{self.kind.title()} Booking for: {self.user}"
