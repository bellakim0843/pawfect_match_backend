from rest_framework import serializers
from users.models import User
from sitters.models import Sitter
from medias.serializers import PhotoSerializer


class BookingSitterSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Sitter
        fields = (
            "name",
            "country",
            "city",
            "rating",
            "photos",
        )
