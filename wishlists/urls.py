from django.urls import path
from .views import WishlistView, WishlistDetail, WishlistToggle

urlpatterns = [
    path("", WishlistView.as_view()),
    path("<int:pk>", WishlistDetail.as_view()),
    path("<int:pk>/sitters/<int:sitter_pk>", WishlistToggle.as_view()),
    # path("<int:pk>/boarders/<int:boarder_pk>", WishlistToggle.as_view()),
]
