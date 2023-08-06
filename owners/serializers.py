# from rest_framework import serializers
# from .models import Owner
# from users.serializers import TinyUserSerializer, UserSerializer
# from categories.serializers import CategorySerializer
# from medias.serializers import PhotoSerializer


# class TinyOwnerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Owner
#         fields = (
#             "pk",
#             "name",
#             "account",
#         )


# class OwnerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Owner
#         fields = "__all__"


# class OwnerDetailSerializer(serializers.ModelSerializer):
#     account = UserSerializer(read_only=True)

#     class Meta:
#         model = Owner
#         fields = "__all__"


# # class PetSerializer(serializers.ModelSerializer):
# #     owner = TinyOwnerSerializer(read_only=True)

# #     class Meta:
# #         model = Pet
# #         fields = (
# #             "pk",
# #             "petname",
# #             "sex",
# #             "age",
# #             "weight",
# #             "breed",
# #             "neutering",
# #             "description",
# #             "owner",
# #         )
