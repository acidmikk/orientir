from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.
from django.utils.safestring import mark_safe

from .models import *


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(label='Текст новости', widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'image_img', 'published')
    list_display_links = ('title', 'content', 'image')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    form = NewsAdminForm

    def image_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100"/>')
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('title', 'avatar', 'image_img', 'position')
    list_display_links = ('title', 'image_img')
    search_fields = ('title', 'content')

    def image_img(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="100"/></a>')
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class ProjectAdminForm(forms.ModelForm):
    content = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Project
        fields = '__all__'


@admin.register(Project)
class ExplorationAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'image_img', 'file', 'published')
    list_display_links = ('title', 'content', 'image')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    form = ProjectAdminForm

    def image_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100"/></a>')
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Photo)
class PhotoAlbum(admin.ModelAdmin):
    list_display = ('image', 'image_img')
    list_display_links = ('image', 'image_img')

    def image_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100"/></a>')
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class AboutAdminForm(forms.ModelForm):
    content1 = forms.CharField(label='Текст новости', widget=CKEditorUploadingWidget(), max_length=3000)
    content2 = forms.CharField(label='Текст новости', widget=CKEditorUploadingWidget(), max_length=3000)
    content3 = forms.CharField(label='Текст новости', widget=CKEditorUploadingWidget(), max_length=3000)
    history = forms.CharField(label='Текст истории', widget=CKEditorUploadingWidget(), max_length=3000)

    class Meta:
        model = About
        fields = '__all__'


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('history', 'content1', 'content2', 'content3')
    list_display_links = ()
    form = AboutAdminForm


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'image_img')
    list_display_links = ('title', 'content', 'image', 'image_img')

    def image_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100"/></a>')
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


@admin.register(Smi)
class SmiAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'link', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'link')
    prepopulated_fields = {'slug': ('title',)}
