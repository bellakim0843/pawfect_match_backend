from django.conf import settings
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from django.db import transaction
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import BoarderService, Boarder
from .serializers import BoarderServiceSerializer
from categories.models import Category
from . import serializers
from .serializers import BoarderDetailSerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from bookings.models import Booking
from bookings.serializers import PublicBookingSerializer, CreateBoarderBookingSerializer


class Boarders(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_boarders = Boarder.objects.all()
        serializer = serializers.BoarderListSerializer(
            all_boarders, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.BoarderDetailSerializer(data=request.data)
        if serializer.is_valid():
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError("Category is required.")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindChoices.DAYCARE:
                    raise ParseError("The category kind should be 'BOARDING'")
            except Category.DoesNotExist:
                raise ParseError("Category not found")
            try:
                with transaction.atomic():
                    boarder = serializer.save(
                        account=request.user,
                        category=category,
                    )
                    boarder_services = request.data.get("boarder_services")
                    for boarder_service_pk in boarder_services:
                        boarder_service = BoarderService.objects.get(
                            pk=boarder_service_pk
                        )
                        boarder.boarder_services.add(boarder_service)
                    serializer = serializers.BoarderDetailSerializer(boarder)
                    return Response(serializer.data)
            except Exception:
                raise ParseError("Service not found")
        else:
            return Response(serializer.errors)


class Boarder_services(APIView):
    def get(self, request):
        all_boarders = BoarderService.objects.all()
        serializer = serializers.BoarderServiceSerializer(all_boarders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.BoarderServiceSerializer(data=request.data)
        if serializer.is_valid():
            boarder_service = serializer.save()
            return Response(serializer.data)  # Return the serialized data directly
        else:
            return Response(serializer.errors)


class Boarder_serviceDetail(APIView):
    def get_object(self, pk):
        try:
            return BoarderService.objects.get(pk=pk)
        except BoarderService.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        boarder_service = self.get_object(pk)
        serializer = serializers.BoarderServiceSerializer(boarder_service)
        return Response(serializer.data)

    def put(self, request, pk):
        boarder_service = self.get_object(pk)
        serializer = serializers.BoarderServiceSerializer(
            boarder_service, data=request.data, partial=True
        )
        if serializer.is_valid():
            updated_boarder_service = serializer.save()
            return Response(BoarderServiceSerializer(updated_boarder_service).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        boarder_service = self.get_object(pk)
        boarder_service.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class BoarderDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Boarder.objects.get(pk=pk)
        except Boarder.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        boarder = self.get_object(pk)
        serializer = serializers.BoarderDetailSerializer(
            boarder, context={"request": request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        boarder = self.get_object(pk)
        if boarder.boarder_account != request.user:
            raise PermissionDenied()
        serializer = serializers.BoarderDetailSerializer(
            boarder, data=request.data, partial=True
        )
        if serializer.is_valid():
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError("Category is required")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.category_kind != Category.CategoryKindChoices.DAYCARE:
                    raise ParseError("Category kind should be daycare")
            except Category.DoesNotExist:
                raise ParseError("Category does not exist")
            try:
                with transaction.atomic():
                    updated_boarder = serializer.save(
                        account=request.user, category=category
                    )
                    boarder_services = request.data.get("services")
                    if boarder_services:
                        updated_boarder.boarder_services.clear()
                        for boarder_service_pk in boarder_services:
                            boarder_service = BoarderService.objects.get(
                                pk=boarder_service_pk
                            )
                            updated_boarder.boarder_services.add(boarder_service)
                    serializer = serializers.BoarderDetailSerializer(updated_boarder)
                    return Response(serializer.data)
            except Exception:
                raise ParseError("Can't update boarder")
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        boarder = self.get_object(pk)
        if boarder.boarder_account != request.user:
            raise PermissionDenied()
        boarder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BoarderReviews(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Boarder.objects.get(pk=pk)
        except Boarder.DoesNotExist:
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
        boarder = self.get_object(pk)
        serializer = serializers.ReviewSerializer(
            boarder.reviews.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = serializers.ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(
                user=request.user,
                boarder=self.get_object(pk),
            )
            serializer = serializers.ReviewSerializer(review)
            return Response(serializer.data)


class BoarderPhotos(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Boarder.objects.get(pk=pk)
        except Boarder.DoesNotExist:
            raise NotFound()

    def post(self, request, pk):
        boarder = self.get_object(pk)
        if request.user != boarder.boarder_account:
            raise PermissionDenied()
        serializer = serializers.PhotoSerializer(data=request.data)
        if serializer.is_valid():
            boarder_photo = serializer.save(boarder=boarder)
            serializer = serializers.PhotoSerializer(boarder_photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class BoarderBookings(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Boarder.objects.get(pk=pk)
        except:
            raise NotFound()

    def get(self, request, pk):
        boarder = self.get_object(pk)
        now = timezone.localtime(timezone.now()).date()
        bookings = Booking.objects.filter(
            boarder=boarder,
            kind=Booking.BookingKindChoices.BOARDER,
            check_in__gt=now,
        )
        serializer = PublicBookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        boarder = self.get_object(pk)
        serializer = CreateBoarderBookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save(
                boarder=boarder,
                user=request.user,
                kind=Booking.BookingKindChoices.BOARDER,
            )
            serializer = PublicBookingSerializer(booking)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
