from django.db import models
from common.models import CommonModel


# Create your models here.
class Boarder(CommonModel):
    boarder_name = models.CharField(
        max_length=80,
    )
    boarder_country = models.CharField(
        max_length=50,
        default="Ireland",
    )
    boarder_city = models.CharField(
        max_length=80,
        default="Dublin",
    )
    boarder_price = models.PositiveIntegerField()
    boarder_address = models.CharField(
        max_length=200,
        default="",
    )
    boarder_description = models.TextField(default="")

    boarder_services = models.ManyToManyField("boarders.BoarderService")

    boarder_category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="boarders",
    )

    boarder_account = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="boarders",
        default=None,
    )

    def __str__(self):
        return f"{self.boarder_name} / {self.boarder_price}"

    def boarder_total_services(self):
        return self.boarder_services.count()

    def rating(self):
        count = self.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            total_rating = 0
            for review in self.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)


class BoarderService(CommonModel):
    service_name = models.CharField(max_length=150)
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.service_name
