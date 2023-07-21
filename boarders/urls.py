from django.urls import path
from . import views

urlpatterns = [
    path("", views.Boarders.as_view()),
    path("<int:pk>", views.BoarderDetail.as_view()),
    path("<int:pk>/reviews", views.BoarderReviews.as_view()),
    path("<int:pk>/photos", views.BoarderPhotos.as_view()),
    path("<int:pk>/bookings", views.BoarderBookings.as_view()),
    path("services/", views.Boarder_services.as_view()),
    path("services/<int:pk>", views.Boarder_serviceDetail.as_view()),
]
