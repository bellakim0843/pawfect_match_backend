from django.db import models
from common.models import CommonModel


class Owner(CommonModel):
    class GenderChoices(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"
        NOT_SPECIFIED = "not_specified", "Prefer not to say"

    profile_photo = models.ImageField(blank=True)
    name = models.CharField(max_length=150, default="")
    gender = models.CharField(
        max_length=30, choices=GenderChoices.choices, default=GenderChoices.MALE
    )
    account = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="owner",
    )

    def __str__(self):
        return self.name

    def total_pets(self):
        return self.pets.count()


class Pet(CommonModel):
    class SpeciesChoices(models.TextChoices):
        DOG = "dog", "Dog"
        CAT = "cat", "Cat"
        ETC = "etc", "Other"

    class SexChoices(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    petname = models.CharField(max_length=80)
    species = models.CharField(
        max_length=20,
        choices=SpeciesChoices.choices,
    )
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
