from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import UserData


@admin.register(UserData)
class UserDataAdmin(ImportExportModelAdmin):
    list_display = ('name', 'phone_number','email')
