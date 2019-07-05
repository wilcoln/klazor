from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render
from django.shortcuts import redirect
from klazor.models import *
import io
import base64
import json


def welcome(request):
    mooc_courses = MoocCourse.objects.all()
    school_courses = SchoolCourse.objects.all()
    folders = Folder.objects.filter(parent_id=1, id__gt=1)  # We remove the root folder
    folder_free_sheets = Sheet.objects.filter(folder=1) # sheets libre de tout dossier
    free_sheets = [sheet for sheet in folder_free_sheets if
                   not hasattr(sheet, 'item')]  # sheets libre de tout dossier ET non Item
    file_items = FileItem.objects.filter(folder=1)
    return render(request, 'pages/welcome.html', {
        'mooc_courses': mooc_courses,
        'school_courses': school_courses,
        'folders': folders,
        'free_sheets': free_sheets,
        'file_items': file_items
    })


def view_mooc_course(request, id):
    mooc_course = MoocCourse.objects.get(pk=id)
    return render(request, 'pages/mooc_course.html', {'mooc_course': mooc_course})


def view_school_course(request, id):
    school_course = SchoolCourse.objects.get(pk=id)
    return render(request, 'pages/school_course.html', {'school_course': school_course})


def view_mooc_course_element(request, id):
    course_element = CourseElement.objects.get(pk=id)
    return render(request, 'pages/mooc_course_element.html', {'course_element': course_element})


# Manages mooc course item nav
def mooc_course_element_reach(request, course_part_id, element_sequence):
    course_part = CoursePart.objects.get(pk=course_part_id)
    try:
        course_element = course_part.courseelement_set.all()[element_sequence-1]
        return render(request, 'pages/mooc_course_element.html', {'course_element': course_element})
    except IndexError:
        return render(request, 'pages/mooc_course.html', {'mooc_course':  course_part.course.mooccourse})


def view_school_course_element(request, id):
    course_element = CourseElement.objects.get(pk=id)
    return render(request, 'pages/school_course_element.html', {'course_element': course_element})


# Manages school course item nav
def school_course_element_reach(request, course_part_id, element_sequence):
    course_part = CoursePart.objects.get(pk=course_part_id)
    try:
        course_element = course_part.courseelement_set.all()[element_sequence - 1]
        return render(request, 'pages/school_course_element.html', {'course_element': course_element})
    except IndexError:
        return render(request, 'pages/school_course.html', {'school_course': course_part.course.schoolcourse})


def view_folder(request, id):
    if id == 1:
        return welcome(request)
    sheets = Sheet.objects.filter(folder=id)
    file_items = FileItem.objects.filter(folder=id)
    folder = Folder.objects.get(pk=id)
    return render(request, 'pages/folder.html', {'folder': folder, 'sheets': sheets, 'file_items': file_items})


def view_folder_editor(request, id, sheet_id):
    if id == 1:
        return welcome(request)
    active_sheet = Sheet.objects.get(pk=sheet_id)
    sheets = Sheet.objects.filter(folder=id)
    folder = Folder.objects.get(pk=id)
    file_items = FileItem.objects.filter(folder=id)
    return render(request, 'pages/folder_editor.html', {'folder': folder, 'active_sheet': active_sheet, 'sheets': sheets, 'file_items': file_items})


def view_sheet(request, id):
    sheet = Sheet.objects.get(pk=id)
    return render(request, 'pages/sheet.html', {'sheet': sheet, 'edit_mode': False})


def new_sheet(request):
    new_sheet = Sheet()
    new_sheet.title = "Nouveau titre"
    new_sheet.save()
    return redirect('sheet', new_sheet.id)


def save_cell(request, id):
    data = json.loads(request.body)
    cell_dict = json.loads(data['cell'])  # Contains modified data and is a dictionary
    sheet = Sheet.objects.get(pk=id)  # The saved sheet, and is instance of Sheet

    storage = FileSystemStorage()
    if 'video' in cell_dict:
        filename = str(cell_dict['filename'])
        video_cell = VideoCell()
        video_cell.sheet = sheet
        video_cell.sequence = cell_dict['sequence']
        video_cell.title = cell_dict['title']
        video_cell.scale = cell_dict['scale']
        video_cell.video.save(filename, storage.open('videos/'+filename))
        video_cell.save()
        storage.delete('videos/' + filename)
    elif 'image' in cell_dict:
        filename = str(cell_dict['filename'])
        image_cell = ImageCell()
        image_cell.sheet = sheet
        image_cell.sequence = cell_dict['sequence']
        image_cell.title = cell_dict['title']
        image_cell.scale = cell_dict['scale']
        image_cell.image.save(filename, storage.open('images/'+filename))
        image_cell.save()
        storage.delete('images/' + filename)
    elif 'audio' in cell_dict:
        filename = str(cell_dict['filename'])
        audio_cell = AudioCell()
        audio_cell.sheet = sheet
        audio_cell.sequence = cell_dict['sequence']
        audio_cell.title = cell_dict['title']
        audio_cell.audio.save(filename, storage.open('audios/'+filename))
        audio_cell.save()
        storage.delete('audios/' + filename)
    elif 'text' in cell_dict:
        markdown_cell = MarkdownCell()
        markdown_cell.sheet = sheet
        markdown_cell.sequence = cell_dict['sequence']
        markdown_cell.text = cell_dict['text']
        markdown_cell.save()

    return HttpResponse(str(cell_dict))


def delete_sheet(request, id):
    sheet = Sheet.objects.get(pk=id)
    sheet.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def save_sheet(request, id):
    sheet = Sheet.objects.get(pk=id)
    sheet.title = request.POST['title']
    # retrieve all old cells
    old_cells = sheet.cell_set.all()
    # Delete all old cells
    for old_cell in old_cells:
        old_cell.delete()
    sheet.save()
    return HttpResponse("success")


def delete_folder(request, id):
    folder = Folder.objects.get(pk=id)
    folder.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


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
    folder.parent_id = request.POST['parent-id']
    folder.name = request.POST['folder-name']
    folder.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def add_folder_files(request):
    folder_id = request.POST['folder-id']
    folder = Folder.objects.get(pk=folder_id)
    files = request.FILES.getlist('files')
    for file in files:
        file_item = FileItem()
        file_item.folder = folder
        file_item.file = file
        file_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def remove_folder_file(request, id):
    file_item = FileItem.objects.filter(pk=id)
    file_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def new_folder_sheet(request, id):
    new_sheet = Sheet()
    new_sheet.title = "Nouveau titre"
    new_sheet.save()
    folder = Folder.objects.get(pk=id)
    new_sheet.folder = folder
    new_sheet.save()
    return redirect('folder-editor', folder.id, new_sheet.id)


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


def toggle_course_element_status(request, id):
    item = CourseElement.objects.get(pk=id)
    item.completed = not item.completed
    item.save()
    return redirect(request.META.get('HTTP_REFERER'))


# Test pdf generation
def print_sheet(request, id):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileItemResponse sets the Cell-Disposition header so that browsers
    # present the option to save the file.
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

