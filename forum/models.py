from django.db import models
from django.urls import reverse


class Board(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=250, unique=True)
    published = models.DateField(db_index=True, verbose_name='Дата публикации', auto_created=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Доски'
        verbose_name = 'Доска'
        ordering = ['-published']


class Topic(models.Model):
    subject = models.CharField(max_length=250, verbose_name='Заголовок')
    last_update = models.DateField(db_index=True, verbose_name='Дата публикации', auto_created=True, auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('topic', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Темы'
        verbose_name = 'Тема'
        ordering = ['-last_update']
