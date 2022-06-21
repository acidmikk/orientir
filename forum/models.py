from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Board(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок', unique=True)
    description = models.TextField(verbose_name='Описание', max_length=500)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    published = models.DateField(db_index=True, verbose_name='Дата публикации', auto_created=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:board_topics', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Доски'
        verbose_name = 'Доска'
        ordering = ['-published']


class Topic(models.Model):
    subject = models.CharField(max_length=255, verbose_name='Заголовок', unique=True)
    subtitle = models.CharField(max_length=500, verbose_name='Описание', unique=True, default='')
    last_update = models.DateField(db_index=True, verbose_name='Последнее изменение', auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('forum:topic_posts', kwargs={'slug': self.slug, 'board_slug': self.board.slug})

    class Meta:
        verbose_name_plural = 'Темы'
        verbose_name = 'Тема'
        ordering = ['-last_update']


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('forum:topic_posts', kwargs={'id': self.id})

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
        ordering = ['-created_at']
