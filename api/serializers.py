from rest_framework.serializers import ModelSerializer, FileField

from api.models import Video


class VideoSerializer(ModelSerializer):
    file = FileField(write_only=True)

    class Meta:
        model = Video
        fields = ["id", "file"]
