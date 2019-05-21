import os
import json
from django.core.files.base import ContentFile
from django.core.files.storage import Storage, FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files import File
from klazor.models import *
import base64
from klazor.settings import MEDIA_ROOT
from klazor.settings import BASE_DIR


def welcome(request):
    mooc_courses = MoocCourse.objects.all()
    school_courses = SchoolCourse.objects.all()
    folders = Folder.objects.filter(parent_id=1, id__gt=1)  # We remove the root folder
    folder_free_sheets = Sheet.objects.filter(folder__sheet_set__folder__isnull=True) | Sheet.objects.filter(
        folder__sheet_set__folder__id=1)  # sheets libre de tout dossier
    free_sheets = [sheet for sheet in folder_free_sheets if
                   not hasattr(sheet, 'item')]  # sheets libre de tout dossier ET non Item
    return render(request, 'pages/welcome.html', {
        'mooc_courses': mooc_courses,
        'school_courses': school_courses,
        'folders': folders,
        'free_sheets': free_sheets,
    })


def view_mooc_course(request, id):
    mooc_course = MoocCourse.objects.get(pk=id)
    return render(request, 'pages/mooc_course.html', {'mooc_course': mooc_course})


def view_school_course(request, id):
    school_course = SchoolCourse.objects.get(pk=id)
    return render(request, 'pages/school_course.html', {'school_course': school_course})


def view_mooc_course_item(request, id):
    mooc_course_item = Item.objects.get(pk=id)
    return render(request, 'pages/mooc_course_item.html', {'mooc_course_item': mooc_course_item})


def view_school_course_item(request, id):
    school_course_item = Item.objects.get(pk=id)
    return render(request, 'pages/school_course_item.html', {'school_course_item': school_course_item})


def view_folder(request, id):
    if id == 1:
        return welcome(request)
    folder = Folder.objects.get(pk=id)
    return render(request, 'pages/folder.html', {'folder': folder})


def view_sheet(request, id):
    sheet = Sheet.objects.get(pk=id)
    return render(request, 'pages/sheet.html', {'sheet': sheet, 'edit_mode': False})


def new_sheet(request):
    new_sheet = Sheet()
    new_sheet.title = "Nouveau titre"
    new_sheet.save()
    return render(request, 'pages/sheet.html', {'sheet': new_sheet, 'edit_mode': True})


def save_content(request, id):
    data = json.loads(request.body)
    content_dict = json.loads(data['content'])  # Contains modified data and is a dictionary
    sheet = Sheet.objects.get(pk=id)  # The saved sheet, and is instance of Sheet
    # retrieve all old contents
    old_contents = sheet.content_set.all()
    # Delete all old contents
    for old_content in old_contents:
        old_content.delete()

    storage = FileSystemStorage()
    if 'video' in content_dict:
        filename = str(content_dict['filename'])
        video_content = VideoContent()
        video_content.sheet = sheet
        video_content.sequence = content_dict['sequence']
        video_content.title = content_dict['title']
        video_content.video.save(filename, storage.open('videos/'+filename))
        video_content.save()
    elif 'image' in content_dict:
        filename = str(content_dict['filename'])
        image_content = ImageContent()
        image_content.sheet = sheet
        image_content.sequence = content_dict['sequence']
        image_content.title = content_dict['title']
        image_content.image.save(filename, storage.open('images/'+filename))
        image_content.save()
    elif 'audio' in content_dict:
        filename = str(content_dict['filename'])
        audio_content = AudioContent()
        audio_content.sheet = sheet
        audio_content.sequence = content_dict['sequence']
        audio_content.title = content_dict['title']
        audio_content.audio.save(filename, storage.open('audios/'+filename))
        audio_content.save()
    elif 'text' in content_dict:
        markdown_content = MarkdownContent()
        markdown_content.sheet = sheet
        markdown_content.sequence = content_dict['sequence']
        markdown_content.text = content_dict['text']
        markdown_content.save()

    return HttpResponse(str(content_dict))


def delete_sheet(request, id):
    sheet = Sheet.objects.get(pk=id)
    sheet.delete()
    return redirect('welcome')


def save_sheet(request, id):
    sheet = Sheet.objects.get(pk=id)
    sheet.title = request.POST['title']
    sheet.save()
    return HttpResponse("success")


def delete_folder(request, id):
    folder = Folder.objects.get(pk=id)
    folder.delete()
    return redirect('welcome')


def delete_mooc_course(request, id):
    mooc_course = MoocCourse.objects.get(pk=id)
    mooc_course.delete()
    return redirect('welcome')


def delete_school_course(request, id):
    school_course = SchoolCourse.objects.get(pk=id)
    school_course.delete()
    return redirect('welcome')


def new_folder(request):
    folder = Folder()
    folder.parent_id = 1
    folder.name = "Nouveau dossier " + str(Folder.objects.latest('id').id + 1)
    folder.save()
    return redirect('welcome')


def upload(request):
    data = request.POST['file']
    if ';base64,' in data:
        filename = request.POST['title'].lower().replace(' ', '_')
        format, file_str = data.split(';base64,')
        ext = format.split('/')[-1]
        storage = FileSystemStorage()
        path = ''
        filename = filename + '.' + ext
        if 'image' in format:
            path = 'images/' + filename
        elif 'audio' in format:
            path = 'audios/' + filename
        elif 'video' in format:
            path = 'videos/' + filename
        if not storage.exists(path):
            storage.save(path, ContentFile(base64.b64decode(file_str)))
        return HttpResponse(filename)
    return HttpResponse('no_new_name')
