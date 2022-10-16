from django.urls import include, path

from .views import *

urlpatterns = [
    path("", index_view, name="index"),
    path("success/", success_view, name="success"),
    path("visitors/", VisitorView.as_view(), name="visitors"),
]