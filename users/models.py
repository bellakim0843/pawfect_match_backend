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
