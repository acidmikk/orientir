from django.urls import path, include
from .views import *
from .feeds import LatestFeedRSS

urlpatterns = [
    path('news/', include([
        path('<slug:slug>', new, name='new'),
        path('', NewsList.as_view(), name='news'),
    ])),
    path('projects/', include([
        path('<slug:slug>', project, name='project'),
        path('', ProjectsList.as_view(), name='projects'),
    ])),
    path('about-us/', include([
        path('', about, name='about'),
    ])),
    path('galleries/', include([
        path('<slug:slug>', gallery, name='gallery'),
        path('', GalleriesList.as_view(), name='galleries'),
    ])),
    path('smi/', SmiList.as_view(), name='smi'),
    path('search/', SearchList.as_view(), name='search'),
    path('contact/', contact_view, name='contact'),
    path('lastnews/', LatestFeedRSS(), name='rss'),
    path('', main, name='main'),
]
