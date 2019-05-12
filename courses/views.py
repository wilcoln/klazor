from django.shortcuts import render
from courses.models import *

from django.shortcuts import HttpResponse


def welcome(request):
    return render(request, 'welcome.html', {'courses': Course.objects.all()})


def add_course(request):
    return render(request, 'add_course.html', {'instructors': Instructor.objects.all()})


def add_instructor(request):
    return render(request, 'add_instructor.html')


def save_course(request):
    response = HttpResponse()
    response.write("Ok")

    itype = request.POST.get('type')
    title = request.POST.get('title')
    instructorId = request.POST.get('instructor')
    if itype == 'school':
        schoolCourse = SchoolCourse()
        schoolCourse.title = title
        lien = ACourseInstructor()
        schoolCourse.year = request.POST.get('year')
        schoolCourse.semester = request.POST.get('semester')
        schoolCourse.save()
        lien.instructor = Instructor.objects.get(pk=instructorId)
        lien.course = schoolCourse
        lien.save()
    else:
        moocCourse = MoocCourse()
        moocCourse.title = title
        lien = ACourseInstructor()
        moocCourse.save()
        lien.instructor = Instructor.objects.get(pk=instructorId)
        lien.course = moocCourse
        lien.save()

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
        notschool = NonSchool()
        notschool.title = title
        notschool.link = link
        notschool.save()

    return response
