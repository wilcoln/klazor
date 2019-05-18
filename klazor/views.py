from django.shortcuts import render
from klazor.models import *


def welcome(request):
    mooc_courses = MoocCourse.objects.all()
    school_courses = SchoolCourse.objects.all()
    folders = Folder.objects.filter(parent_id=1, id__gt=1) # We remove the root folder
    folder_free_sheets = Sheet.objects.filter(folder__sheet_set__folder__isnull=True) | Sheet.objects.filter(folder__sheet_set__folder__id=1)  # sheets libre de tout dossier
    free_sheets = [sheet for sheet in folder_free_sheets if not hasattr(sheet, 'item')]  # sheets libre de tout dossier ET non Item
    return render(request, 'pages/welcome.html', {
        'mooc_courses': mooc_courses,
        'school_courses': school_courses,
        'folders': folders,
        'free_sheets': free_sheets
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
    if id==1:
        return welcome(request)
    folder = Folder.objects.get(pk=id)
    return render(request, 'pages/folder.html', {'folder': folder})


def view_sheet(request, id):
    sheet = Sheet.objects.get(pk=id)
    return render(request, 'pages/sheet.html', {'sheet': sheet})
