from django import forms
from django.contrib.admin import register, ModelAdmin

from .models import Post, Comment


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ("title", "creating_date", "vote", "author")
    list_filter = ("id", "title", "creating_date", "vote", "author")
    search_fields = ("id", "title", "author")

    class Meta:
        model = Post
        fields = "__all__"


@register(Comment)
class CommentAdmin(ModelAdmin):
    description = forms.CharField(label="Comment")
    list_display = ("post", "content", "author_name", "creating_date")
    list_filter = ("post", "content", "author_name", "creating_date")
    search_fields = ("id", "post")

    class Meta:
        model = Comment
        fields = "__all__"
