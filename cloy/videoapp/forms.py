from django.forms import ModelForm      
from .models import Video
from django import forms
from .validations import video_size

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields= ['video',]