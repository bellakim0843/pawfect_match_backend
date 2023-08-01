from django.contrib import admin
from .models import Owner

# admin action


# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "account",
        "pet_name",
        "pet_gender",
        "pet_age",
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


# @admin.register(Pet)
# class PetAdmin(admin.ModelAdmin):
#     list_display = (
#         "petname",
#         "sex",
#         "age",
#         "weight",
#         "neutering",
#     )

#     list_filter = (
#         "age",
#         "weight",
#         "neutering",
#     )
