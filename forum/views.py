from itertools import chain

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.conf import settings
from django.contrib.auth.models import User

from .models import *


def index(request):
    return HttpResponse("Hello world!")
