from django.db import models
from common.models import CommonModel


# Create your models here.
class Photo(CommonModel):
    file = models.URLField()
    description = models.CharField(
        max_length=140,
    )

    # boarder = models.ForeignKey(
    #     "boarders.Boarder",
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    #     related_name="photos",
    # )
    sitter = models.ForeignKey(
        "sitters.Sitter",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self):
        return f"File name :{self.file}"

    # Video
    # class Video(CommonModel):
    #
    #    file = models.FileField()
    #    sitter = models.OneToOneField(
    #   "sitters.Sitter"
    #    on_delete = models.CASCADE
    # )
