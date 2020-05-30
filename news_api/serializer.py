from rest_framework import serializers

from .models import Post, Comment


class CommentParentSerializer(serializers.ModelSerializer):
    """Comment serializer"""
    post = serializers.SlugRelatedField(slug_field='title', read_only=True)
    post_link = serializers.SerializerMethodField('get_link_from_post')

    class Meta:
        model = Comment
        fields = ("id", "post", "post_link", "content", "author_name", "creating_date")

    def get_link_from_post(self, comment):
        post_link = comment.post.link
        return post_link


class CommentSerializer(serializers.ModelSerializer):
    """Comment serializer"""

    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    """Post serializer"""

    class Meta:
        model = Post
        fields = "__all__"


class PostDetailSerializer(serializers.ModelSerializer):
    """Post detail serializer"""
    comments = CommentParentSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"


class VotePostSerializer(serializers.ModelSerializer):
    """Vote the post"""

    class Meta:
        model = Post
        fields = ("id", "vote")

    def update(self, instance, validated_data):
        instance.vote += 1
        instance.save()
        return instance
