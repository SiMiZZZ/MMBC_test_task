from django.contrib import admin
from django.urls import path, include
from .views import UploadFileAPIView




urlpatterns = [
    path("file/", UploadFileAPIView.as_view({"post": "create"}), name="Upload File"),
    path("file/<pk>", UploadFileAPIView.as_view({"patch": "update", "get": "retrieve", "delete": "destroy"}),
         name="Start crop File"),

]
