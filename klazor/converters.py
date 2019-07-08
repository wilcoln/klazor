from klazor.models import *
import copy

def folder_to_course(folder):
    course = Course()
    course.title = folder.name
    return course

def folder_to_mooc_course(folder):
    mooc_course = MoocCourse()
    mooc_course.user = folder.user
    mooc_course.title = folder.name
    mooc_course.save()
    course_parts = []
    for i, subfolder in enumerate(folder.folder_set.all()):
        course_part = CoursePart()
        course_part.sequence = i+1
        course_part.level = 1
        course_part.label, course_part.title = subfolder.name.split(':')
        course_part.course = mooc_course
        course_part.save()
        for j, sheet in enumerate(subfolder.item_set.all()):
            course_element = CourseElement()
            course_element.sequence = j+1
            course_element.user = sheet.user
            course_element.course_part = course_part
            course_element.title = sheet.title
            course_element.save()
            for cell in sheet.cell_set.all():
                cell.sheet = course_element
                cell.pk = None
                cell.save()
    return mooc_course
