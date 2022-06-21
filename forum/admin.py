from django.contrib import admin
from django import forms
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


class TopicAdminForm(forms.ModelForm):
    subtitle = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Topic
        fields = '__all__'


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'last_update', 'board', 'starter')
    list_display_links = ('subject', 'last_update')
    search_fields = ('subject', 'last_update')
    prepopulated_fields = {'slug': ('subject',)}
    form = TopicAdminForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('message', 'topic', 'created_at', 'created_by')
    list_display_links = ('message', 'topic')
    search_fields = ('message', 'topic', 'created_at', 'created_by')
