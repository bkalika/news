from rest_framework import viewsets

from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer, VotePostSerializer, PostDetailSerializer


class PostViewSet(viewsets.ModelViewSet):
    """GET, POST, PUT, DELETE the Post model"""

    queryset = Post.objects.all()
    action_serializers = {
        'retrieve': PostDetailSerializer,
        'list': PostSerializer,
        'update': PostSerializer,
    }

    def get_serializer_class(self):
        if self.action == 'list':
            return PostSerializer
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """GET, POST, PUT, DELETE the Comment model"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class VotePostViewSet(viewsets.ModelViewSet):
    """Vote the comment"""
    queryset = Post.objects.all()
    serializer_class = VotePostSerializer
