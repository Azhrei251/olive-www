from django.urls import include, path

from .views import index_view, success_view

urlpatterns = [
    path("", index_view, name="index"),
    path("success/", success_view, name="success"),
]