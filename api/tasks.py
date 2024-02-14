import os
import time
from celery import shared_task
import ffmpeg
@shared_task(name="crop_video_file")
def crop_file(file_path: str, width: int, height: int):
    path_without_ext = os.path.splitext(file_path)[0]
    (ffmpeg
     .input(file_path)
     .filter('crop', width, height)
     .output(path_without_ext + "_new" + ".mp4")
     .run())
    return True

def test_crop(file_path: str, width: int, height: int):
    path_without_ext = os.path.splitext(file_path)[0]

    (ffmpeg
     .input(file_path)
     .filter('crop', width, height)
     .output(path_without_ext + "_new" + ".mp4")
     .run())
    return True