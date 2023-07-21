from django.db import models
from common.models import CommonModel

# Create your models here.


class Sitter(CommonModel):
    name = models.CharField(
        max_length=80,
    )
    country = models.CharField(
        max_length=50,
        default="Ireland",
    )
    city = models.CharField(
        max_length=80,
        default="Dublin",
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=200,
        default="",
    )
    description = models.TextField(default="")

    services = models.ManyToManyField(
        "sitters.Service",
        related_name="sitters",
    )

    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="sitters",
    )

    account = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="sitters",
    )

    def __str__(self):
        return f"{self.name} / {self.price}"

    def total_services(self):
        return self.services.count()

    def rating(self):
        count = self.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in self.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)


class Service(CommonModel):
    service_name = models.CharField(max_length=150)
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.service_name
