from django.urls import path, include
from .views import *

app_name = 'forum'

urlpatterns = [
    path('', BoardsView.as_view(), name='boards'),
    path('boards/', include([
        path('<slug:board_slug>/topics/<slug:topic_slug>/reply/', reply_topic, name='reply_topic'),
        path('<slug:board_slug>/topics/<slug:slug>', TopicView.as_view(), name='topic_posts'),
        path('<slug:slug>', TopicsView.as_view(), name='board_topics'),
    ])),
]
