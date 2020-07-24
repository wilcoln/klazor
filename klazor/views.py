from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.shortcuts import redirect
from klazor.models import *
import json

# Organize all these views into CourseView, SheetView, FolderView, CellView, FileView


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def welcome(request):
    if request.user.is_authenticated:
        quick_access = Sheet.objects.filter(owner_id=request.user.id).order_by('-updated_at')[:6]
        root_folder = Folder.objects.get(pk=1)
        folders = Folder.objects.filter(parent_id=1, owner_id=request.user.id)  # We remove the root folder
        free_sheets = Sheet.objects.filter(folder=1, owner_id=request.user.id)
        file_items = FileItem.objects.filter(folder=1, owner_id=request.user.id)
        return render(
            request, 'pages/welcome.html', {
                'quick_access': quick_access,
                'folder': root_folder,
                'sub_folders': folders,
                'sheets': free_sheets,
                'file_items': file_items
            }
        )
    return redirect('/login')


def view_folder(request, id):
    if id == 1:
        return redirect('welcome')
    sheets = Sheet.objects.filter(folder=id)
    file_items = FileItem.objects.filter(folder=id)
    folder = Folder.objects.get(pk=id)
    sub_folders = folder.sub_folder_set.all()
    return render(
        request, 'pages/folder.html', {
            'folder': folder,
            'sub_folders': sub_folders,
            'sheets': sheets,
            'file_items': file_items
        }
    )


def view_folder_editor(request, id, sheet_id):
    active_sheet = Sheet.objects.get(pk=sheet_id)
    sheets = Sheet.objects.filter(folder=id)
    folder = Folder.objects.get(pk=id)
    file_items = FileItem.objects.filter(folder=id)
    return render(
        request, 'pages/folder_editor.html', {
            'folder': folder,
            'active_sheet': active_sheet,
            'sheets': sheets,
            'file_items': file_items
        }
    )


def view_sheet(request, id):
    sheet = Sheet.objects.get(pk=id)
    return render(request, 'pages/sheet.html', {'sheet': sheet})


def save_cell(request, id):
    data = json.loads(request.body)
    cell_dict = json.loads(data['cell'])  # Contains modified data and is a dictionary
    sheet = Sheet.objects.get(pk=id)  # The saved sheet, and is instance of Sheet

    cell_type = cell_dict['type']
    if cell_type == 'VIDEO':
        video_cell = VideoCell()
        video_cell.sheet = sheet
        video_cell.sequence = cell_dict['sequence']
        video_cell.title = cell_dict['title']
        video_cell.scale = cell_dict['scale']
        video_cell.url = cell_dict['url']
        video_cell.save()
    elif cell_type == 'IMAGE':
        image_cell = ImageCell()
        image_cell.sheet = sheet
        image_cell.sequence = cell_dict['sequence']
        image_cell.title = cell_dict['title']
        image_cell.scale = cell_dict['scale']
        image_cell.url = cell_dict['url']
        image_cell.save()
    elif cell_type == 'AUDIO':
        audio_cell = AudioCell()
        audio_cell.sheet = sheet
        audio_cell.sequence = cell_dict['sequence']
        audio_cell.title = cell_dict['title']
        audio_cell.url = cell_dict['url']
        audio_cell.save()
    elif cell_type == 'MARKDOWN':
        markdown_cell = MarkdownCell()
        markdown_cell.sheet = sheet
        markdown_cell.sequence = cell_dict['sequence']
        markdown_cell.text = cell_dict['text']
        markdown_cell.save()
    elif cell_type == 'YOUTUBE':
        youtube_cell = YoutubeCell()
        youtube_cell.sheet = sheet
        youtube_cell.sequence = cell_dict['sequence']
        youtube_cell.url = cell_dict['url']
        youtube_cell.title = cell_dict['title']
        youtube_cell.scale = cell_dict['scale']
        youtube_cell.save()
    elif cell_type == 'FILE':
        file_cell = FileCell()
        file_cell.sheet = sheet
        file_cell.sequence = cell_dict['sequence']
        file_cell.title = cell_dict['title']
        file_cell.url = cell_dict['url']
        file_cell.save()
    elif cell_type == 'NUMERICAL_INPUT':
        numerical_question_cell = NumericalInputCell()
        numerical_question_cell.sheet = sheet
        numerical_question_cell.sequence = cell_dict['sequence']
        numerical_question_cell.answer = cell_dict['answer']
        numerical_question_cell.save()
    elif cell_type == 'OPEN_ENDED_INPUT':
        open_ended_question_cell = OpenEndedInputCell()
        open_ended_question_cell.sheet = sheet
        open_ended_question_cell.sequence = cell_dict['sequence']
        open_ended_question_cell.answer = cell_dict['answer']
        open_ended_question_cell.save()
    elif cell_type == 'MULTIPLE_CHOICE_INPUT':
        multiple_choice_question_cell = MultipleChoiceInputCell()
        multiple_choice_question_cell.sheet = sheet
        multiple_choice_question_cell.sequence = cell_dict['sequence']
        multiple_choice_question_cell.save()
        propositions = cell_dict['propositions']
        for proposition_dict in propositions:
            proposition = Proposition()
            proposition.input_cell = multiple_choice_question_cell
            proposition.statement = proposition_dict['statement']
            proposition.is_true = proposition_dict['isTrue']
            proposition.save()

    return HttpResponse(str(cell_dict))


def delete_item(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def save_sheet(request, id):
    sheet = Sheet.objects.get(pk=id)
    sheet.name = request.POST['name']
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


def add_folder(request):
    folder = Folder()
    folder.owner = request.user
    folder.parent_id = request.POST['parent-id']
    folder.name = request.POST['folder-name']
    folder.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def add_tag(request):
    tag = Tag()
    tag.name = request.POST['tag-name']
    tag.save()
    tag_dict = {'id': tag.id, 'name': tag.name}
    return HttpResponse(json.dumps(tag_dict))


def rename_folder(request, id):
    folder = Folder.objects.get(pk=id)
    folder.name = request.POST['folder-name']
    folder.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def move_item(request, id, destination_id):
    item = Item.objects.get(pk=id)
    item.folder_id = destination_id
    item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def move_folder(request, id, destination_id):
    folder = Folder.objects.get(pk=id)
    folder.parent_id = destination_id
    folder.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def add_folder_files(request):
    folder_id = request.POST['folder-id']
    folder = Folder.objects.get(pk=folder_id)
    files = request.FILES.getlist('files')
    for file in files:
        file_item = FileItem()
        file_item.folder = folder
        file_item.owner = request.user
        file_item.name = file.name
        file_item.file = file
        file_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def add_sheet(request, id):
    new_sheet = Sheet()
    new_sheet.name = "Nouveau titre"
    new_sheet.owner = request.user
    folder = Folder.objects.get(pk=id)
    new_sheet.folder = folder
    new_sheet.save()
    if id == 1:
        return redirect('sheet', new_sheet.id)
    else:
        return redirect('folder-editor', folder.id, new_sheet.id)
