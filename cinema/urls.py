from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import GenreViewSet

app_name = "cinema"
router = DefaultRouter()
router.register("genres", viewset=GenreViewSet, basename="genres")
urlpatterns = [
    path("", include(router.urls)),
]
