from django.urls import path
from rest_framework import routers

from .views import (
    NodeListView,
    NodeUpdateView,
    NodeDetailView,
    NodeDeleteView,
    NodeCreateView,
)

urlpatterns = [
    path("<int:pk>/edit/", NodeUpdateView.as_view(), name="node_edit"),
    path("<int:pk>/", NodeDetailView.as_view(), name="node_detail"),
    path("<int:pk>/delete/", NodeDeleteView.as_view(), name="node_delete"),
    path("new/", NodeCreateView.as_view(), name="node_new"),
    path("", NodeListView.as_view(), name="node_list"),
]
