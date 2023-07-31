from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import CommonModel


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

    # pet = models.ForeignKey(
    #     "users.Pet",
    #     on_delete=models.CASCADE,
    #     related_name="pets",
    #     null=True,
    # )

    def __str__(self):
        return f"{self.name}"


# class Pet(models.Model):
#     class SexChoices(models.TextChoices):
#         MALE = "male", "Male"
#         FEMALE = "female", "Female"

#     petname = models.CharField(
#         max_length=80,
#         null=True,
#         blank=True,
#     )
#     sex = models.CharField(
#         null=True,
#         blank=True,
#         max_length=20,
#         choices=SexChoices.choices,
#     )
#     age = models.PositiveIntegerField(
#         null=True,
#         blank=True,
#     )
#     weight = models.PositiveIntegerField(
#         null=True,
#         blank=True,
#     )
#     breed = models.CharField(
#         null=True,
#         blank=True,
#         max_length=80,
#     )
#     neutering = models.BooleanField(default=False)
#     description = models.TextField(default="")
#     user = models.ForeignKey(
#         "users.User",
#         on_delete=models.CASCADE,
#         related_name="users",
#         null=True,
#     )

#     def __str__(self):
#         return self.petname
