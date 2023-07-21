from django.db import models
from common.models import CommonModel


# Create your models here.
class Category(CommonModel):
    class CategoryKindChoices(models.TextChoices):
        DAYCARE = ("daycare", "Daycare")
        BOARDING = ("boading", "Boarding")

    category_name = models.CharField(max_length=80)
    category_kind = models.CharField(
        max_length=30,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self):
        return f"{self.category_kind.title()}: {self.category_name}"

    class Meta:
        verbose_name_plural = "Categories"
