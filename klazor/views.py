import json

from django.shortcuts import render
from django.shortcuts import redirect
from klazor.models import *
from django.http import HttpResponse
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile


def welcome(request):
    mooc_courses = MoocCourse.objects.all()
    school_courses = SchoolCourse.objects.all()
    folders = Folder.objects.filter(parent_id=1, id__gt=1)  # We remove the root folder
    folder_free_sheets = Sheet.objects.filter(folder__sheet_set__folder__isnull=True) | Sheet.objects.filter(folder__sheet_set__folder__id=1)  # sheets libre de tout dossier
    free_sheets = [sheet for sheet in folder_free_sheets if not hasattr(sheet, 'item')]  # sheets libre de tout dossier ET non Item
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


def save_sheet(request, id):
    data = json.loads(request.body.decode('utf-8'))
    sheet_dict = json.loads(data['sheet'])  # Contains modified data and is a dictionary
    sheet = Sheet.objects.get(pk=id)  # The saved sheet, and is instance of Sheet
    # retrieve all old contents
    old_contents = sheet.content_set.all()

    # create new content and associate
    sheet.title = sheet_dict['title'] # sauvegarde le titre
    if sheet_dict['contents']:
        for content_dict in sheet_dict['contents']:
            content = Content()
            if 'video' in content_dict:
                content = VideoContent()
                content.sheet = sheet
                content.title = content_dict['title']
                if "/media" in content_dict['video']:
                    content.video = content_dict['video']
                else:
                    format, videostr = content_dict['video'].split(';base64,')
                    ext = format.split('/')[-1]
                    filename = content_dict['title'].lower().replace(' ', '_') + '.' + ext
                    content.video = ContentFile(base64.b64decode(videostr), name=filename)

            elif 'image' in content_dict:
                content = ImageContent()
                content.sheet = sheet
                content.title = content_dict['title']
                if "/media" in content_dict['image']:
                    content.image = content_dict['image']
                else:
                    format, imagestr = content_dict['image'].split(';base64,')
                    ext = format.split('/')[-1]
                    filename = content_dict['title'].lower().replace(' ', '_') + '.' + ext
                    content.image = ContentFile(base64.b64decode(imagestr), name=filename)

            elif 'audio' in content_dict:
                content = AudioContent()
                content.sheet = sheet
                content.title = content_dict['title']
                if "/media" in content_dict['audio']:
                    content.audio = content_dict['audio']
                else:
                    format, audiostr = content_dict['audio'].split(';base64,')
                    ext = format.split('/')[-1]
                    filename = content_dict['title'].lower().replace(' ', '_') + '.' + ext
                    content.audio = ContentFile(base64.b64decode(audiostr), name=filename)

            elif 'text' in content_dict:
                content = MarkdownContent()
                content.sheet = sheet
                content.text = content_dict['text']
            content.save()

    # Delete all old contents
    for content in old_contents:
        content.delete()
    sheet.save()

    return HttpResponse(str(sheet))


def delete_sheet(request, id):
    sheet = Sheet.objects.get(pk=id)
    sheet.delete()
    return redirect('welcome')


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