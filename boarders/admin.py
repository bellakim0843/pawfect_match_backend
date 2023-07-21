from django.contrib import admin
from .models import Boarder, BoarderService

# Register your models here.


@admin.action(description="Apply Promotion rate")
def promo_prices(model_admin, request, boarders):
    for boarder in boarders.all():
        boarder.boarder_price = boarder.boarder_price * 0.7
        boarder.save()


@admin.register(Boarder)
class BoarderAdmin(admin.ModelAdmin):
    actions = (promo_prices,)

    list_display = (
        "boarder_name",
        "boarder_country",
        "boarder_city",
        "boarder_price",
        "rating",
        "boarder_total_services",
    )

    list_filter = (
        "boarder_country",
        "boarder_city",
        "boarder_price",
    )

    search_fields = (
        "boarder_name",
        "boarder_country",
        "boarder_city",
    )


@admin.register(BoarderService)
class BoarderServiceAdmin(admin.ModelAdmin):
    list_display = (
        "service_name",
        "description",
    )
