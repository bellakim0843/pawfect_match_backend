from rest_framework.serializers import ModelSerializer
from sitters.serializers import SitterListSerializer
from .models import Wishlist


class WishlistSerializer(ModelSerializer):
    sitters = SitterListSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Wishlist
        fields = (
            "pk",
            "name",
            "sitters",
        )
