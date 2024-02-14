from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from .models import Video
@receiver(pre_delete, sender=Video)
def image_model_delete(sender, instance, **kwargs):
    if instance.file.name:
        instance.file.delete(False)