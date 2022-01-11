from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import django.utils.timezone as timezone
from mptt.models import MPTTModel, TreeForeignKey

from users.models import CustomUser

class Bubble(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.CharField(max_length=255)
    radius = models.SmallIntegerField(default=1)
    citing_patents_count = models.SmallIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("bubble_detail", args=[str(self.id)])

class Node(MPTTModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    priority = models.SmallIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name='authoredNodes')
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name='childNodes',
        null=True,
        blank=True
    )



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("node_detail", args=[str(self.id)])


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="comments",)
    comment = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("node_list")
