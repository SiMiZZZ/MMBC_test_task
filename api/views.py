from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, JSONParser
from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Video
from .tasks import crop_file
from api.serializers import VideoSerializer
from celery import current_app
from celery.result import AsyncResult

class UploadFileAPIView(ModelViewSet):
    parser_classes = (MultiPartParser, JSONParser)
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.filter(id=self.kwargs.get('pk'))

    def create(self, request, *args, **kwargs):
        """ Create video file

        Only MP4 extension is supported

        """
        return super().create(request, *args, **kwargs)

    def update(self, request, pk=None, **kwargs):
        """
        Update the  Video entity by cropping

        body params:
        - width: int
        - height: int
        :return: Bool value of correct upload task of cropping
        """
        width = self.request.data.get("width", None)
        height = self.request.data.get("height", None)
        if not (width and height):
            return Response({"error": "Not found correct data parameters"}, status=status.HTTP_400_BAD_REQUEST)
        file = self.get_object()
        print(file)
        result = crop_file.apply_async((file.file.path, width, height, ))
        file.last_crop_task_id = result.task_id
        file.save()
        return Response({"success": True}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, **kwargs):
        """
        Get information about Video Entity and about last cropping task of it

        url parameters:
        - pk: str

        :return: Video entity date
        """
        file = get_object_or_404(Video.objects, id=pk)
        if file.last_crop_task_id:
            result = AsyncResult(file.last_crop_task_id)
            print(result)
            data = {
                "id": file.id,
                "filename": file.file.name,
                "processing": not result.ready(),
                "processingSuccess": result.successful()
            }
        else:
            data = {
                "id": file.id,
                "filename": file.file.name,
                "processing": None,
                "processingSuccess": None
            }
        return Response(data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
        Delete Video Entity by id

        :return: Bool value about success delete
        """
        return super().destroy(request, *args, **kwargs)


