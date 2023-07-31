import time
from django.shortcuts import get_object_or_404

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
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db import transaction
from django.conf import settings
from django.utils import timezone


from .models import Service, Sitter
from categories.models import Category
from . import serializers
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from bookings.models import Booking
from bookings.serializers import PublicBookingSerializer, CreateSitterBookingSerializer
from .serializers import SitterDetailSerializer


class Services(APIView):
    def get(self, request):
        all_services = Service.objects.all()
        serializer = serializers.ServiceSerializer(all_services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ServiceSerializer(data=request.data)
        if serializer.is_valid():
            service = serializer.save()
            return Response(
                serializers.ServiceSerializer(service).data,
            )
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class ServiceDetail(APIView):
    def get_object(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        service = self.get_object(pk)
        serializer = serializers.ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, pk):
        service = self.get_object(pk)
        serializer = serializers.ServiceSerializer(
            service, data=request.data, partial=True
        )
        if serializer.is_valid():
            updated_service = serializer.save()
            return Response(
                serializers.ServiceSerializer(updated_service).data,
            )
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        service = self.get_object(pk)
        service.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Sitters(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_sitters = Sitter.objects.all()
        serializer = serializers.SitterListSerializer(
            all_sitters,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.SitterDetailSerializer(data=request.data)
        if serializer.is_valid():
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError("Category is required.")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.category_kind == Category.CategoryKindChoices.BOARDING:
                    raise ParseError("The category kind should be 'Daycare'")
            except Category.DoesNotExist:
                raise ParseError("Category not found")

            try:
                with transaction.atomic():
                    sitter = serializer.save(
                        account=request.user,
                        category=category,
                    )
                    services = request.data.get("services")
                    for service_pk in services:
                        try:
                            service = Service.objects.get(pk=service_pk)
                            sitter.services.add(service)
                        except Service.DoesNotExist:
                            raise ParseError("Service not found")

                    serializer = serializers.SitterDetailSerializer(sitter)
                    return Response(serializer.data)
            except Exception as e:
                raise ParseError(str(e))
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class SitterDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Sitter.objects.get(pk=pk)
        except Sitter.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        sitter = self.get_object(pk)
        serializer = serializers.SitterDetailSerializer(
            sitter, context={"request": request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        sitter = self.get_object(pk)
        if sitter.account != request.user:
            raise PermissionDenied()
        serializer = SitterDetailSerializer(sitter, data=request.data, partial=True)
        if serializer.is_valid():
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError("Category is required")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.category_kind == Category.CategoryKindChoices.BOARDING:
                    raise ParseError("Category kind should be daycare")
            except Category.DoesNotExist:
                raise ParseError("Category does not exist")
            try:
                with transaction.atomic():
                    updated_sitter = serializer.save(
                        account=request.user, category=category
                    )
                    services = request.data.get("services")
                    if services:
                        updated_sitter.services.clear()
                        for service_pk in services:
                            service = Service.objects.get(pk=service_pk)
                            updated_sitter.services.add(service)
                    serializer = SitterDetailSerializer(updated_sitter)
                    return Response(serializer.data)
            except:
                raise ParseError("Can't update sitter")
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        sitter = self.get_object(pk)
        if sitter.account != request.user:
            raise PermissionDenied()
        sitter.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class SitterReviews(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Sitter.objects.get(pk=pk)
        except Sitter.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        sitter = self.get_object(pk)
        serializer = ReviewSerializer(
            sitter.reviews.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(
                user=request.user,
                sitter=self.get_object(pk),
            )
            serializer = ReviewSerializer(review)
            return Response(serializer.data)


class SitterPhotos(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Sitter.objects.get(pk=pk)
        except Sitter.DoesNotExist:
            raise NotFound()

    def post(self, request, pk):
        sitter = self.get_object(pk)
        if request.user != sitter.account:
            raise PermissionDenied()
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(sitter=sitter)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class SitterBookings(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Sitter, pk=pk)

    def get(self, request, pk):
        sitter = self.get_object(pk)
        now = timezone.localtime(timezone.now()).date()
        bookings = Booking.objects.filter(
            sitter=sitter,
            kind=Booking.BookingKindChoices.SITTER,
            check_in__gte=now,
        )
        serializer = PublicBookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        sitter = self.get_object(pk)
        serializer = CreateSitterBookingSerializer(
            data=request.data,
            context={"sitter": sitter},
        )
        if serializer.is_valid():
            # Ensure that the user making the request is authenticated
            if not request.user.is_authenticated:
                return Response(
                    {"detail": "Authentication credentials were not provided."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            booking = serializer.save(
                sitter=sitter,
                kind=Booking.BookingKindChoices.SITTER,
                user=request.user,
            )
            serializer = PublicBookingSerializer(booking)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            # Return detailed errors in case of validation failure
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class SitterBookingCheck(APIView):
    def get_object(self, pk):
        try:
            return Sitter.objects.get(pk=pk)
        except:
            raise NotFound()

    def get(self, request, pk):
        sitter = self.get_object(pk)
        check_out = request.query_params.get("check_out")
        check_in = request.query_params.get("check_in")
        exists = Booking.objects.filter(
            sitter=sitter,
            check_in__lte=check_out,
            check_out__gte=check_in,
        ).exists()
        if exists:
            return Response({"ok": False})
        return Response({"ok": True})
