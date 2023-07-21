from django.contrib import admin
from .models import Chatroom, Message


# Register your models here.
@admin.register(Chatroom)
class ChatroomAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "created_at",
        "updated_at",
    )

    list_filter = ("created_at",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "chat_text",
        "chat_user",
        "chat_boarder",
        "created_at",
    )

    list_filter = ("created_at",)
