from django.db import models
from cloudinary.models import CloudinaryField
from .validations import video_size
from django.core.validators import FileExtensionValidator




class Video(models.Model):
    allowed_extensions=['MOV','avi','mp4','webm','mkv']
    video= CloudinaryField('video', resource_type='video', validators=[video_size, FileExtensionValidator(allowed_extensions=allowed_extensions)])