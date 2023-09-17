from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from exampleapp.api import TagViewSet, PostViewSet, CommentViewSet, UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()
router.register("tags", TagViewSet)
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)
router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
