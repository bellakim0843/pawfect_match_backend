from time import sleep
import jwt
import requests
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated
from .models import Pet
from bookings.models import Booking
from bookings.serializers import UserBookingSerializer, PetSerializer
from .serializers import UserSerializer, PrivateUserSerializer
from users.models import User
from . import serializers

# Create your views here.


# class PetView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         # Retrieve pets associated with the authenticated user
#         pets = Pet.objects.filter(user=request.user)
#         serializer = PetSerializer(pets, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         # Create a new pet associated with the authenticated user
#         serializer = PetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
