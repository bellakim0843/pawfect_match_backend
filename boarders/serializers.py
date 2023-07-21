from rest_framework import serializers
from .models import BoarderService, Boarder
from users.serializers import TinyUserSerializer
from reviews.serializers import ReviewSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist


class BoarderServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoarderService
        fields = "__all__"


class BoarderDetailSerializer(serializers.ModelSerializer):
    boarder_account = TinyUserSerializer(read_only=True)
    boarders = BoarderServiceSerializer(read_only=True, many=True)
    boarder_category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()
    is_account = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    boarder_photos = serializers.SerializerMethodField()

    class Meta:
        model = Boarder
        fields = "__all__"

    def get_rating(self, boarder):
        return boarder.rating()

    def get_is_account(self, boarder):
        request = self.context["request"]
        return boarder.boarder_account == request.user

    def get_is_liked(self, obj):
        wishlist = Wishlist.objects.filter(boarders=obj)
        return wishlist.exists()

    def get_boarder_photos(self, boarder):
        photos = boarder.photos.all()
        return PhotoSerializer(photos, many=True).data


class BoarderListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_account = serializers.SerializerMethodField()
    boarder_photos = serializers.SerializerMethodField()

    class Meta:
        model = Boarder
        fields = (
            "pk",
            "boarder_photos",
            "boarder_name",
            "boarder_country",
            "boarder_city",
            "boarder_price",
            "rating",
            "is_account",
        )

    def get_rating(self, boarder):
        return boarder.rating()

    def get_is_account(self, boarder):
        request = self.context["request"]
        return boarder.boarder_account == request.user

    def get_boarder_photos(self, boarder):
        photos = boarder.photos.all()
        return PhotoSerializer(photos, many=True).data
