from django.db import models
from common.models import CommonModel


# Create your models here.
class Wishlist(CommonModel):
    name = models.CharField(max_length=150)
    # boarders = models.ManyToManyField(
    #     "boarders.Boarder",
    #     null=True,
    #     blank=True,
    # )
    sitters = models.ManyToManyField(
        "sitters.Sitter",
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="wishlists",
    )

    def __str__(self):
        return self.name
