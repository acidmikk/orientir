from itertools import chain

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .models import *
from .forms import *


class BoardsView(ListView):
    model = Board
    queryset = Board.objects.all()
    template_name = 'forum/home.html'
    paginate_by = 1
    context_object_name = 'boards'


class TopicsView(ListView):
    template_name = 'forum/board.html'
    paginate_by = 2
    context_object_name = 'topics'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        board = Board.objects.get(slug=self.kwargs['slug'])
        context['title'] = board.title
        context['description'] = board.description
        return context

    def get_queryset(self):
        self.board = get_object_or_404(Board, slug=self.kwargs['slug'])
        return Topic.objects.filter(board=self.board)


class TopicView(ListView):
    template_name = 'forum/topic.html'
    paginate_by = 2
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = Topic.objects.get(slug=self.kwargs['slug'])
        context['title'] = topic.subject
        context['subtitle'] = topic.subtitle
        context['date'] = topic.last_update
        return context

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, slug=self.kwargs['slug'])
        return Post.objects.filter(topic=self.topic)


# @login_required
# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     if request.method == 'POST':
#         form = NewTopicForm(request.POST)
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = board
#             topic.starter = request.user  # <- here
#             topic.save()
#             Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 topic=topic,
#                 created_by=request.user  # <- and here
#             )
#             return redirect('topic_posts', pk=pk, topic_pk=topic.pk)
#     else:
#         form = NewTopicForm()
#     return render(request, 'new_topic.html', {'board': board, 'form': form})


@login_required
def reply_topic(request, board_slug, slug):
    topic = get_object_or_404(Topic, board__slug=board_slug, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=board_slug, topic_pk=slug)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})
