from django.urls import path, include
from .views import *

urlpatterns = [
    path('', BoardsView.as_view(), name='boards'),
    path('boards/<slug:slug>', TopicsView.as_view(), name='board_topics')
]
