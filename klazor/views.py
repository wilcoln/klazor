from django.shortcuts import render
from klazor.models import *

from django.shortcuts import HttpResponse


def welcome(request):
    mooc_courses = MoocCourse.objects.all()
    school_courses = SchoolCourse.objects.all()
    folders = Folder.objects.all()
    # TODO Change this silly query
    free_sheets = Sheet.objects.all()
    return render(request, 'welcome.html', {
        'mooc_courses': mooc_courses,
        'school_courses': school_courses,
        'folders': folders,
        'free_sheets': free_sheets
    })


def view_mooc_course(request, id):
    mooc_course = MoocCourse.objects.get(pk=id)
    return render(request, 'mooc_course.html', {'mooc_course': mooc_course})


def view_school_course(request, id):
    school_course = SchoolCourse.objects.get(pk=id)
    return render(request, 'school_course.html', {'school_course': school_course})


def view_mooc_course_item(request, id):
    mooc_course_item = Item.objects.get(pk=id)
    return render(request, 'mooc_course_item.html', {'mooc_course_item': mooc_course_item})


def view_school_course_item(request, id):
    school_course_item = Item.objects.get(pk=id)
    return render(request, 'school_course_item.html', {'school_course_item': school_course_item})


def view_folder(request, id):
    folder = Folder.objects.get(pk=id)
    return render(request, 'folder.html', {'folder': folder})


def view_sheet(request, id):
    sheet = Sheet.objects.get(pk=id)
    return render(request, 'sheet.html', {'sheet': sheet})