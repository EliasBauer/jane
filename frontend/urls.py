from django.urls import path, re_path

from .views import index

app_name = "frontend"

urlpatterns = [
    path("", index),
    path("master_data", index),
    re_path(".*", index),
]
