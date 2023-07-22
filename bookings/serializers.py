from django.utils import timezone
from rest_framework import serializers
from .models import Booking


class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            # "daycare_day",
            "check_in",
            "check_out",
            "pets",
        )


# class CreateSitterBookingSerializer(serializers.ModelSerializer):
#     daycare_day = serializers.DateField()

#     """
#     check_in = serializers.DateField()
#     check_out = serializers.DateField()
#     """

#     class Meta:
#         model = Booking
#         fields = (
#             # "daycare_day",
#             "check_in",
#             "check_out",
#             "pets",
#         )

#     def validate_daycare_day(self, value):
#         now = timezone.localtime(timezone.now()).date()
#         if now > value:
#             raise serializers.ValidationError("Can't book in the past!")
#         return value

#     """
#     def validate_check_in(self, value):
#         now = timezone.localtime(timezone.now()).date()
#         if now > value:
#             raise serializers.ValidationError("Can't book in the past!")
#         return value

#     def validate_check_out(self, value):
#         now = timezone.localtime(timezone.now()).date()
#         if now > value:
#             raise serializers.ValidationError("Can't book in the past!")
#         return value
#                     """

#     def validate(self, data):
#         sitter = self.context.get("sitter")
#         if data["check_out"] <= data["check_in"]:
#             raise serializers.ValidationError(
#                 "Check in should be smaller than check out."
#             )
#         if Booking.objects.filter(
#             sitter=sitter,
#             check_in__lte=data["check_out"],
#             check_out__gte=data["check_in"],
#         ).exists():
#             raise serializers.ValidationError(
#                 "Those (or some) of those dates are already taken."
#             )
#         return data


class CreateSitterBookingSerializer(serializers.ModelSerializer):
    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            # "daycare_day",
            "check_in",
            "check_out",
            "pets",
        )

    """
    def validate_daycare_day(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value
    """

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
        if data["check_out"] <= data["check_in"]:
            raise serializers.ValidationError(
                "Check in should be smaller than check out."
            )
        if Booking.objects.filter(
            check_in__lte=data["check_out"],
            check_out__gte=data["check_in"],
        ).exists():
            raise serializers.ValidationError(
                "Those (or some) of those dates are already taken."
            )
        return data
