from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "username",
                    "password",
                    "name",
                    "email",
                    "is_sitter",
                    "pet_name",
                    "pet_gender",
                    "pet_age",
                    "pet_weight",
                    "pet_breed",
                    "neutering",
                    "pet_description",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important Dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "name",
        "is_sitter",
        "avatar",
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
