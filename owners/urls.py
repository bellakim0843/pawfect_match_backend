from django.urls import path
from . import views

urlpatterns = [
    path("", views.Owners.as_view()),
    path("<int:pk>", views.OwnerDetail.as_view()),
    path("pets/", views.Pets.as_view()),
    path("pets/<int:pk>", views.PetsDetail.as_view()),
]
