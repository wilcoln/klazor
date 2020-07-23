"""Klazor URL Configuration. """
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from klazor.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Administration views
    path('admin/', admin.site.urls),

    # Authentication views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/welcome.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', welcome, name='welcome'),
    url(r'^register/$', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('folder/<int:id>/', view_folder, name='folder'),
    path('folder/editor/<int:id>/sheet/<int:sheet_id>', view_folder_editor, name='folder-editor'),
    path('sheet/<int:id>/', view_sheet, name='sheet'),
    path('folder/<int:id>/sheet/new/', add_sheet, name='add-sheet'),
    path('sheet/<int:id>/save/', save_sheet, name='save-sheet'),
    path('sheet/<int:id>/cell/save/', save_cell, name='save-cell'),
    path('item/move/<int:id>/into/<int:destination_id>', move_item, name='move-item'),
    path('item/delete/<int:id>/', delete_item, name='delete-item'),
    path('folder/delete/<int:id>/', delete_folder, name='delete-folder'),
    path('folder/move/<int:id>/into/<int:destination_id>', move_folder, name='move-folder'),
    path('folder/rename/<int:id>/', rename_folder, name='rename-folder'),
    path('folder/add/', add_folder, name='add-folder'),
    path('tag/add/', add_tag, name='add-tag'),
    path('folder/file/add/', add_folder_files, name='add-folder-files'),
    # Api urls
    url(r'^api/', include('api.urls')),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
