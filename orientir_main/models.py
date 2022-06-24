from django.db import models
from django.db.models import Q
from django.urls import reverse
from .forms import *
from orientir.settings import MEDIA_URL


class SearchManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(title__icontains=query) | Q(content__icontains=query))
            qs = qs.filter(or_lookup)

        return qs


class News(models.Model):
    title = models.CharField(max_length=60, verbose_name='Заголовок')
    slug = models.SlugField(max_length=90, unique=True)
    content = models.TextField(verbose_name='Текст')
    mini_content = models.TextField(max_length=90, verbose_name='Аннотация')
    published = models.DateField(db_index=True, verbose_name='Дата публикации')
    image = models.ImageField(verbose_name='Заставка новости', upload_to=f'news/%Y/%m/%d/', null=True, blank=True)
    file = models.FileField(verbose_name='Файл презентации в pdf', upload_to=f'news/%Y/%m/%d/', null=True, blank=True)
    objects = SearchManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:new', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ['-published']


class People(models.Model):
    title = models.CharField(max_length=250, verbose_name='Имя')
    content = models.CharField(max_length=120, null=True, blank=True, verbose_name='Короткое описание')
    description = models.TextField(verbose_name='Описание')
    avatar = models.ImageField(upload_to=f'person/%Y/%m/%d/', blank=True, null=True,
                               verbose_name='Фото человека')
    published = models.DateField(db_index=True, verbose_name='Дата публикации')

    # class Position(models.TextChoices):
    #     __empty__ = 'Выберете группу человека'
    #     expert = 'e', 'Экспертный совет'
    #     supervisor = 's', 'Наблюдательный совет'
    #     president = 'p', 'Президент фонда'
    # position = models.CharField(max_length=1, choices=Position.choices, default=Position.__empty__,
    #                            verbose_name='Позиция')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:person', kwargs={'id': self.id})

    class Meta:
        verbose_name_plural = 'Люди'
        verbose_name = 'Человека'


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=120, unique=True)
    content = models.TextField(verbose_name='Текст')
    image = models.ImageField(verbose_name='Заставка проекта', upload_to=f'works/%Y/%m/%d/', null=True, blank=True)
    file = models.FileField(verbose_name='Файл презентации в pdf', upload_to=f'works/%Y/%m/%d/', null=True, blank=True)
    published = models.DateField(db_index=True, verbose_name='Дата публикации')
    objects = SearchManager()

    def get_absolute_url(self):
        return reverse('main:project', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Проекты'
        verbose_name = 'Проект'
        ordering = ['-published']


class Album(models.Model):
    title = models.CharField(max_length=95, verbose_name='Заголовок')
    image = models.ImageField(verbose_name='Фото', upload_to='album/%Y/%m/%d/', null=False, blank=False)
    published = models.DateField(db_index=True, verbose_name='Дата публикации')
    slug = models.SlugField(max_length=95, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:gallery', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Альбомы'
        verbose_name = 'Альбом'
        ordering = ['-published']


class Photo(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='gallery/%Y/%m/%d/', null=False, blank=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Фото'
        verbose_name = 'Фото'
        ordering = ['-album']


class About(models.Model):
    content1 = models.TextField(verbose_name='Текст 1 блока')
    image1 = models.ImageField(verbose_name='Картинка 1', upload_to='about/%Y/%m/%d/', null=False, blank=False)
    content2 = models.TextField(verbose_name='Текст 2 блока')

    class Meta:
        verbose_name_plural = 'Инфо без раздела'
        verbose_name = 'Текст'


class Slider(models.Model):
    title = models.CharField(max_length=50, verbose_name='Основной текст')
    content = models.TextField(verbose_name='Доп текст', max_length=111)
    image = models.ImageField(verbose_name='Картинка', upload_to='other/%Y/%m/%d/', null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Фото на главной'
        verbose_name = 'фото'


class LinksBag(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')
    content = models.TextField(verbose_name='Текст')
    slug = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:links', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Портфель ссылок'
        verbose_name = 'Портфель ссылок'


class Link(models.Model):
    content = models.TextField(verbose_name='Текст')
    link = models.URLField(verbose_name='Ссылка', blank=False, null=False)
    bag = models.ForeignKey(LinksBag, on_delete=models.CASCADE, verbose_name='Портфель')

    class Meta:
        verbose_name_plural = 'Ссылки'
        verbose_name = 'Ссылка'
