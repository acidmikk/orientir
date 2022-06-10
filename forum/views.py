from itertools import chain

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.conf import settings
from django.contrib.auth.models import User

from .models import *


class BoardsView(ListView):
    model = Board
    queryset = Board.objects.all()
    template_name = 'forum/home.html'
    paginate_by = 2


class TopicsView(ListView):
    template_name = 'forum/'
    paginate_by = 2

    def get_queryset(self):
        self.board = get_object_or_404(Board, slug=self.args[0])
        return Topic.objects.filter(board=self.board)
