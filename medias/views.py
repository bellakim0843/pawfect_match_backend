import requests
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
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
        if photo.sitter and photo.sitter.account != request.user:
            raise PermissionDenied()
        photo.delete()
        return Response(status=HTTP_200_OK)


class GetUploadUrl(APIView):
    def post(self, request):
        url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ID}/images/v2/direct_upload"
        uploadImgUrl = requests.post(
            url, headers={"Authorization": f"Bearer {settings.CF_TOKEN}"}
        )
        uploadImgUrl = uploadImgUrl.json()
        result = uploadImgUrl.get("result")
        if result:
            return Response(
                {"id": result.get("id"), "uploadURL": result.get("uploadURL")}
            )
        else:
            return Response(
                {
                    "id": "00000",
                    "uploadURL": "http://127.0.0.1:8000/api/v1/medias/photos/upload-photo",
                }
            )


class UploadPhoto(APIView):
    def post(self, request):
        image_data = request.FILES["file"]
        path = default_storage.save(image_data, ContentFile(image_data.read()))

        return Response({"result": {"id": path}})
