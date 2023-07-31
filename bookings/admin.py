from django.contrib import admin
from .models import Booking


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "kind",
        "sitter",
        "owner",
        "pet",
        "check_in",
        "check_out",
        "pets",
    )

    list_filter = ("kind",)
