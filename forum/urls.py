from django.urls import path, include
from .views import *

app_name = 'forum'

urlpatterns = [
    path('', BoardsView.as_view(), name='boards'),
    path('boards/<slug:slug>', TopicsView.as_view(), name='board_topics')
]
