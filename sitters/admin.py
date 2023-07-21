from django.contrib import admin
from .models import Sitter, Service

# admin action


@admin.action(description="Apply Promotion rate")
def promo_prices(model_admin, request, sitters):
    for sitter in sitters.all():
        sitter.price = sitter.price * 0.7
        sitter.save()


# Register your models here.
@admin.register(Sitter)
class SitterAdmin(admin.ModelAdmin):
    actions = (promo_prices,)

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "rating",
        "total_services",
    )

    list_filter = (
        "country",
        "city",
        "price",
    )

    search_fields = (
        "name",
        "country",
        "city",
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "service_name",
        "description",
        "created_at",
        "updated_at",
    )
