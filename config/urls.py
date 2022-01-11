from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from nodes import views
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(
    title='Node Schema',
    url='api/'
)


router = routers.DefaultRouter()
router.register(r'nodes', views.BubbleView, basename='node')



urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", include_docs_urls("API Docs")),
    path('api/', include(router.urls)),
    path("users/", include("users.urls")),
    path("users/", include("django.contrib.auth.urls")),
    path("nodes/", include("nodes.urls")),
    path("", include("pages.urls")),
    path('hello/', TemplateView.as_view(template_name='hello_webpack.html'), name = "hello"),
    path('nodeSchema/', schema_view),
]
