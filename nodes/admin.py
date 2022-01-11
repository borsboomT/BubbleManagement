from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from django.db import models
from .models import Node, Comment, Bubble


class CommentInline(admin.TabularInline):
    model = Comment

class BubbleAdmin(admin.ModelAdmin):
    model = Bubble


class NodeAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 50
    inlines = [
        CommentInline
    ]



admin.site.register(
    Node,
    NodeAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)
admin.site.register(Comment)
admin.site.register(Bubble,BubbleAdmin)
