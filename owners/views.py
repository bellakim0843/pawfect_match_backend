import time
from django.shortcuts import get_object_or_404
import requests
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
    HTTP_200_OK,
)
from rest_framework.exceptions import NotFound, ParseError, PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.db import transaction
from django.conf import settings
from django.utils import timezone
from . import serializers
from .serializers import OwnerDetailSerializer, OwnerSerializer


from .models import Owner


# class Pets(APIView):
#     def get(self, request):
#         all_pets = Pet.objects.all()
#         serializer = serializers.PetSerializer(all_pets, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = serializers.PetSerializer(data=request.data)
#         if serializer.is_valid():
#             pet = serializer.save()
#             return Response(serializer.data, status=HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# class PetsDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Pet.objects.get(pk=pk)
#         except Pet.DoesNotExist:
#             raise NotFound()

#     def get(self, request, pk):
#         pet = self.get_object(pk)
#         serializer = serializers.PetSerializer(pet)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         pet = self.get_object(pk)
#         serializer = serializers.PetSerializer(pet, data=request.data, partial=True)
#         if serializer.is_valid():
#             updated_service = serializer.save()
#             return Response(
#                 serializers.PetSerializer(updated_service).data,
#             )
#         else:
#             return Response(
#                 serializer.errors,
#                 status=HTTP_400_BAD_REQUEST,
#             )

#     def delete(self, request, pk):
#         pet = self.get_object(pk)
#         pet.delete()
#         return Response(status=HTTP_204_NO_CONTENT)


class Owners(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Owner.objects.get(pk=pk)
        except Owner.DoesNotExist:
            raise NotFound()

    def get(self, request):
        all_owners = Owner.objects.all()
        serializer = serializers.OwnerSerializer(
            all_owners,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.OwnerDetailSerializer(data=request.data)
        if serializer.is_valid():
            pets = request.data.get(
                "pets", []
            )  # Default to an empty list if 'pets' is not provided

            try:
                with transaction.atomic():
                    owner = serializer.save(account=request.user)

                    serializer = serializers.OwnerDetailSerializer(owner)
                    return Response(serializer.data)
            except Exception as e:
                raise ParseError(str(e))
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class OwnerDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Owner.objects.get(pk=pk)
        except Owner.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        user = request.user
        owners = Owner.objects.filter(account=user)
        serializer = OwnerDetailSerializer(owners, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        owner = self.get_object(pk)
        if owner.account != request.user:
            raise PermissionDenied()

        serializer = serializers.OwnerDetailSerializer(
            owner, data=request.data, partial=True
        )
        if serializer.is_valid():
            try:
                updated_owner = serializer.save(account=request.user)
                serializer = serializers.OwnerDetailSerializer(
                    updated_owner, context={"request": request}
                )
                return Response(serializer.data)
            except Exception as e:
                raise ParseError("Can't update sitter: " + str(e))
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        owner = self.get_object(pk)
        if owner.account != request.user:
            raise PermissionDenied()
        owner.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class OwnerMe(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch the owner associated with the logged-in user
        try:
            owner = Owner.objects.get(account=request.user)
            serializer = serializers.OwnerDetailSerializer(owner)
            return Response(serializer.data)
        except Owner.DoesNotExist:
            raise NotFound("Owner not found.")

    def put(self, request):
        # Fetch the owner associated with the logged-in user
        try:
            owner = Owner.objects.get(account=request.user)
        except Owner.DoesNotExist:
            raise NotFound("Owner not found.")

        serializer = serializers.OwnerDetailSerializer(
            owner,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            owner = serializer.save(account=request.user)
            serializer = serializers.OwnerDetailSerializer(owner)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
