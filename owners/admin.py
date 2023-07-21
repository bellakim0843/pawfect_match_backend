from django.contrib import admin
from .models import Owner, Pet

# admin action


# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "gender",
        "profile_photo",
        "account",
        "total_pets",
    )

    list_filter = (
        "name",
        "gender",
        "account",
    )

    search_fields = (
        "name",
        "account",
    )


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        "petname",
        "species",
        "sex",
        "age",
        "weight",
        "neutering",
    )

    list_filter = (
        "species",
        "age",
        "weight",
        "neutering",
    )
