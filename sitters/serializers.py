from rest_framework import serializers
from .models import Service, Sitter
from users.serializers import TinyUserSerializer
from reviews.serializers import ReviewSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            "pk",
            "service_name",
            "description",
        )


class SitterDetailSerializer(serializers.ModelSerializer):
    account = TinyUserSerializer(read_only=True)
    services = ServiceSerializer(
        read_only=True,
        many=True,
    )
    category = CategorySerializer(
        read_only=True,
    )
    rating = serializers.SerializerMethodField()
    is_account = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)  # Add this line

    class Meta:
        model = Sitter
        fields = "__all__"

    def get_rating(self, sitter):
        return sitter.rating()

    def get_is_account(self, sitter):
        request = self.context.get("request")
        if request:
            return sitter.account == request.user
        return False


class SitterListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_account = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Sitter
        fields = (
            "pk",
            "photos",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_account",
            "category",
        )

    def get_rating(self, sitter):
        return sitter.rating()

    # 고치기
    def get_is_account(self, sitter):
        request = self.context["request"]
        return sitter.account == request.user
