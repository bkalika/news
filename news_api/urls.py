from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = format_suffix_patterns(
    [
        path("post/", views.PostViewSet.as_view({"get": "list", "post": "create"})),
        path(
            "post/<int:pk>/",
            views.PostViewSet.as_view(
                {"get": "retrieve", "delete": "destroy", "put": "update", }
            ),
        ),
        path("post/<int:pk>/vote/", views.VotePostViewSet.as_view({"put": "update"})),
        path(
            "comments/",
            views.CommentViewSet.as_view(
                {"get": "list", "post": "create"}
            ),
        ),
        path(
            "comments/<int:pk>/",
            views.CommentViewSet.as_view(
                {"get": "retrieve", "delete": "destroy", "put": "update", "post": "create"}
            ),
        ),
    ]
)
