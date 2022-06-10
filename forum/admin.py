from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from .models import *

# Register your models here.


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}



