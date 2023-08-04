from django.urls import path
from .views import PhotoDetail, UploadPhoto

urlpatterns = [
    path("photos/get-url", UploadPhoto.as_view()),
    path("photos/<int:pk>", PhotoDetail.as_view()),
    path("photos/upload-photo", UploadPhoto.as_view()),
]
