from django.urls.conf import include, path

from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    MovieViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet,
                basename="genres")

router.register("actors", ActorViewSet,
                basename="actors")

router.register("cinema_halls", CinemaHallViewSet,
                basename="cinema_halls")

router.register("movies", MovieViewSet,
                basename="movies")

router.register("movie_sessions", MovieSessionViewSet,
                basename="movie_sessions")


urlpatterns = [
    path("", include(router.urls)),
]
