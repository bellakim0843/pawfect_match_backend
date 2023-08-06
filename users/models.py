from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import CommonModel

# from owners.models import Owner


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    is_sitter = models.BooleanField(default=False)

    avatar = models.URLField(blank=True)

    class PetSexChoices(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    pet_name = models.CharField(max_length=80, default="", null=True, blank=True)

    pet_gender = models.CharField(
        max_length=20,
        choices=PetSexChoices.choices,
        default="male",
        null=True,
        blank=True,
    )
    pet_age = models.PositiveIntegerField(default=0, null=True, blank=True)
    pet_weight = models.PositiveIntegerField(default=0, null=True, blank=True)
    pet_breed = models.CharField(max_length=80, default="", null=True, blank=True)
    neutering = models.BooleanField(default=False, null=True, blank=True)
    pet_description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.name
