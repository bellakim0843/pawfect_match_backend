from django.db import models
from common.models import CommonModel


class Owner(CommonModel):
    class GenderChoices(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"
        NOT_SPECIFIED = "not_specified", "Prefer not to say"

    class PetSexChoices(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    name = models.CharField(max_length=150, default="")
    gender = models.CharField(
        max_length=30, choices=GenderChoices.choices, default=GenderChoices.MALE
    )

    # 여기부터 추가

    # pet = models.ForeignKey(
    #     "owners.Pet",
    #     null=True,
    #     blank=True,
    #     on_delete=models.CASCADE,
    #     related_name="owners_pet",
    # )

    account = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="owners",
    )

    pet_name = models.CharField(max_length=80, default="")

    pet_gender = models.CharField(
        max_length=20,
        choices=PetSexChoices.choices,
        default="male",
    )
    pet_age = models.PositiveIntegerField(default=0)
    pet_weight = models.PositiveIntegerField(default=0)
    pet_breed = models.CharField(max_length=80, default="")
    neutering = models.BooleanField(default=False)
    pet_description = models.TextField(default="")

    def __str__(self):
        return self.name
