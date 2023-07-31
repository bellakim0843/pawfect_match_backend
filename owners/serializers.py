from rest_framework import serializers
from .models import Owner, Pet
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer


class TinyOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = (
            "pk",
            "name",
            "account",
        )


class OwnerSerializer(serializers.ModelSerializer):
    pet = serializers.SerializerMethodField()

    class Meta:
        model = Owner
        fields = (
            "pk",
            "name",
            "gender",
            "account",
            "pet",
        )

    def get_pet(self, obj):
        return PetSerializer(obj.pet).data


class OwnerDetailSerializer(serializers.ModelSerializer):
    account = TinyUserSerializer(read_only=True)
    pets = serializers.SerializerMethodField()

    class Meta:
        model = Owner
        fields = "__all__"

    def get_pets(self, obj):
        return PetSerializer(obj.pets.all(), many=True).data


class PetSerializer(serializers.ModelSerializer):
    owner = TinyOwnerSerializer(read_only=True)

    class Meta:
        model = Pet
        fields = (
            "pk",
            "petname",
            "sex",
            "age",
            "weight",
            "breed",
            "neutering",
            "description",
            "owner",
        )
