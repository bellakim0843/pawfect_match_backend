from django.db import models
from common.models import CommonModel


# Create your models here.
class Chatroom(CommonModel):
    chat_users = models.ManyToManyField(
        "users.User",
    )

    def __str__(self):
        return "Chatting Room"


class Message(CommonModel):
    chat_text = models.TextField()
    chat_user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="messengers",
    )
    chat_sitter = models.ForeignKey(
        "messengers.Chatroom",
        on_delete=models.CASCADE,
        related_name="messengers",
    )

    def __str__(self):
        return f"{self.chat_user} says: {self.chat_text}"
