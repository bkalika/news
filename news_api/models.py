from datetime import datetime

from django.db import models


class Post(models.Model):
    """Post"""

    title = models.CharField("Title", max_length=150)
    link = models.SlugField("Link", max_length=260, unique=True)
    creating_date = models.DateTimeField("Creating date", default=datetime.now)
    vote = models.SmallIntegerField(
        "Amount of votes", default=0, help_text="to vote the post"
    )
    author = models.CharField("Author", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        unique_together = ["title", "link"]
        ordering = ["-vote"]


class Comment(models.Model):
    """Comment"""

    author_name = models.CharField("Author", max_length=150)
    content = models.TextField("Content", max_length=500)
    creating_date = models.DateTimeField("Creating date", default=datetime.now)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name="post",
        related_name="comments",
        null=True,
    )

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-creating_date"]
