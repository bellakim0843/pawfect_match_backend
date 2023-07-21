import requests
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import Photo

# Create your views here.


class PhotoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise NotFound()

        # or (
        #    photo.boarder and photo.boarder.account != request.user

    def delete(self, request, pk):
        photo = self.get_object(pk)
        if (photo.sitter and photo.sitter.account != request.user) or (
            photo.boarder and photo.boarder.boarder_account != request.user
        ):
            raise PermissionDenied()
        photo.delete()
        return Response(status=HTTP_200_OK)
