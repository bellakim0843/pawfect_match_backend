from django.urls import path
from . import views

urlpatterns = [
    path("", views.Sitters.as_view()),
    path("<int:pk>", views.SitterDetail.as_view()),
    path("<int:pk>/reviews", views.SitterReviews.as_view()),
    path("<int:pk>/photos", views.SitterPhotos.as_view()),
    path("<int:pk>/bookings", views.SitterBookings.as_view()),
    path("<int:pk>/bookings/check", views.SitterBookingCheck.as_view()),
    path("services/", views.Services.as_view()),
    path("services/<int:pk>", views.ServiceDetail.as_view()),
]
