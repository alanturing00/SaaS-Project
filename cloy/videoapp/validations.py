from django.core.exceptions import ValidationError
import os
from django.conf import settings

def video_size(instan):
    size= instan.size
    if size > 20000000:
        raise ValidationError("maximum size is about 200 MB!")
    
def addfunc(file_name, itorater, text, time, during):
    # if the main directory not exists, then create it:
    if not os.path.exists(settings.SRT_FILES_DIR):
                os.makedirs(settings.SRT_FILES_DIR)

    # remove the file name video extention and add the .srt extention:
    first_dot_index = file_name.find('.')
    if first_dot_index != -1:
        file_name = file_name[:first_dot_index]
    else:
        file_name = file_name
    file_name+= '.srt'

    # defin the file path:
    file_path = os.path.join(settings.SRT_FILES_DIR, file_name)

    #  if the file exists, then add to it, else, create one:
    file_mode = 'a' if os.path.exists(file_path) else 'w'

    with open(file_path, file_mode) as file:
        file.write(f"{itorater}\n{time} --> {during}\n{text}\n\n")
    
    return file_name