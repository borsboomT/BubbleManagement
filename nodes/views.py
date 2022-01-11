from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .serializers import BubbleSerializer
from rest_framework import viewsets
from .models import Node, Bubble


class BubbleView(viewsets.ModelViewSet):
    serializer_class = BubbleSerializer
    queryset = Bubble.objects.all()

class NodeListView(LoginRequiredMixin, ListView):
    model = Node
    template_name = "node_list.html"
    login_url = "login"


class NodeDetailView(LoginRequiredMixin, DetailView):
    model = Node
    template_name = "node_detail.html"
    login_url = "login"


class NodeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Node
    fields = (
        "title",
        "body",
    )
    template_name = "node_edit.html"
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.author != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


class NodeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Node
    template_name = "node_delete.html"
    success_url = reverse_lazy("node_list")
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.author != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


class NodeCreateView(LoginRequiredMixin, CreateView):
    model = Node
    template_name = "node_new.html"
    fields = ("title", "body")
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
