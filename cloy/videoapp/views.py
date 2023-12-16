from django.shortcuts import render
from .forms import VideoForm
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .validations import addfunc

def home(request):
    return render(request, 'videoapp/base.html')

def uploader(request):
    form= VideoForm()
    if request.method== 'POST':
        video_form= VideoForm(data= request.POST, files=request.FILES)
        action= request.POST.get('action')

        if action== 'srtsubmit':
            # get the itorater, text, time, and durition values:
            itorater= request.POST.get('itorater')
            text= request.POST.get('text')
            time= request.POST.get('time')
            during= request.POST.get('during')
            file_name= request.POST.get('file_name')
            filename= addfunc(file_name, itorater, text, time, during)
        
        if action== "set_coordinate":
            # get the coordinate valuse:
            x= request.POST.get("x")
            y= request.POST.get("y")
            z= request.POST.get("z")

        if action== 'videosubmit':
            
            if video_form.is_valid():
                video= video_form.save()
                video.save()
                video_url = video.video.url
                public_id = video.video.public_id
                return render(request,'videoapp/upload.html', {"video_url":video_url, "public_id":public_id})
        
        
    else:
        form= VideoForm()
    return render(request,'videoapp/upload.html', {'form':form})



