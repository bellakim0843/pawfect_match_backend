from typing import Any, List, Optional, Tuple
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


class ReviewFilter(admin.SimpleListFilter):
    title = "Review Filter"

    parameter_name = "filtering"

    def lookups(self, request, model_admin):
        return [
            ("bad", "Bad Review (<3)"),
            ("neutral", "Neutral Review (=3)"),
            ("good", "Good Review (>3)"),
        ]

    def queryset(self, request, reviews):
        result = self.value()
        match = {
            "good": reviews.filter(rating__gt=3),
            "bad": reviews.filter(rating__lt=3),
            "neutral": reviews.filter(rating__exact=3),
        }
        return match.get(result, reviews)


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        WordFilter,
        ReviewFilter,
        "rating",
        "user__is_sitter",
    )
