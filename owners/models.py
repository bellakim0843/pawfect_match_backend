from django.db import models
from common.models import CommonModel


class Owner(CommonModel):
    class GenderChoices(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"
        NOT_SPECIFIED = "not_specified", "Prefer not to say"

    name = models.CharField(max_length=150, default="")
    gender = models.CharField(
        max_length=30, choices=GenderChoices.choices, default=GenderChoices.MALE
    )

    # 여기부터 추가

    pet = models.ForeignKey(
        "owners.Pet",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="owners_pet",
    )

    account = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="owners",
    )

    def __str__(self):
        return self.name

    def total_pets(self):
        return self.pets.count()


class Pet(CommonModel):
    class SexChoices(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    petname = models.CharField(max_length=80)

    sex = models.CharField(
        max_length=20,
        choices=SexChoices.choices,
    )
    age = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    breed = models.CharField(
        max_length=80,
    )
    neutering = models.BooleanField()
    description = models.TextField(default="")
    owner = models.ForeignKey(
        "owners.Owner",
        on_delete=models.CASCADE,
        related_name="pets",
    )

    def __str__(self):
        return self.petname
