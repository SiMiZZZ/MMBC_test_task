import uuid
from django.db import models
from api.validators import validate_file_extension

class Video(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    file = models.FileField(upload_to='videos/', validators=[validate_file_extension])
    last_crop_task_id: str = models.CharField(max_length=30, null=True, blank=True)

