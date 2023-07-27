from django.utils import timezone
from rest_framework import serializers
from .models import Booking
from common.serializers import BookingSitterSerializer
from users.serializers import TinyUserSerializer


class PublicBookingSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "pets",
            "user",
        )


class CreateSitterBookingSerializer(serializers.ModelSerializer):
    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "pets",
        )

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't check in the past!")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't check out the past!")
        return value

    def validate(self, data):
        sitter = self.context.get("sitter")
        if data["check_out"] <= data["check_in"]:
            raise serializers.ValidationError(
                "Check in should be smaller than check out."
            )
        if Booking.objects.filter(
            sitter=sitter,
            check_in__lte=data["check_out"],
            check_out__gte=data["check_in"],
        ).exists():
            raise serializers.ValidationError(
                "Those (or some) of those dates are already taken."
            )
        return data


class UserBookingSerializer(serializers.ModelSerializer):
    sitter = BookingSitterSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "pets",
            "sitter",
        )


class SitterBookingSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "pets",
            "user",
        )
