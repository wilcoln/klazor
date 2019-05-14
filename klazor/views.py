from django.shortcuts import render
from klazor.models import *

from django.shortcuts import HttpResponse


def welcome(request):
    mooc_courses = MoocCourse.objects.all()
    school_courses = SchoolCourse.objects.all()
    return render(request, 'welcome.html', {
        'mooc_courses': mooc_courses,
        'school_courses': school_courses
    })


def view_mooc_course(request, id):
    mooc_course = MoocCourse.objects.get(pk=id)
    return render(request, 'mooc_course.html', {'mooc_course': mooc_course})


def view_school_course(request, id):
    school_course = SchoolCourse.objects.get(pk=id)
    return render(request, 'school_course.html', {'school_course': school_course})


def add_course(request):

    return render(request, 'add_course.html', {'instructors': Instructor.objects.all()})


def add_instructor(request):
    return render(request, 'add_instructor.html')


def save_course(request):
    response = HttpResponse()
    response.write("Ok")

    itype = request.POST.get('type')
    title = request.POST.get('title')
    instructor_id = request.POST.get('instructor')
    if itype == 'school':
        school_course = SchoolCourse()
        school_course.title = title
        school_course.year = request.POST.get('year')
        school_course.semester = request.POST.get('semester')
        school_course.save()
        school_course.instructors.add(Instructor.objects.get(pk=instructor_id))
        school_course.save()
    else:
        mooc_course = MoocCourse()
        mooc_course.title = title
        mooc_course.instructors.add(Instructor.objects.get(pk=instructor_id))
        mooc_course.save()

    return response


def save_instructor(request):
    response = HttpResponse()
    response.write("Ok")

    itype = request.POST.get('type')
    title = request.POST.get('title')
    link = request.POST.get('link')
    if itype == 'school':
        school = School()
        school.title = title
        school.link = link
        school.admissions_link = request.POST.get('admissions-link')
        school.programs_link = request.POST.get('programs-link')
        school.save()
    else:
        notschool = NotSchool()
        notschool.title = title
        notschool.link = link
        notschool.save()

    return response
