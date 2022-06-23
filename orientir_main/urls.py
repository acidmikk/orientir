from django.urls import path, include
from .views import *
from .feeds import LatestFeedRSS

app_name = 'main'

urlpatterns = [
    path('news/', include([
        path('<slug:slug>', new, name='new'),
        path('', NewsList.as_view(), name='news'),
    ])),
    path('projects/', include([
        #path('portfolio_of_links/antikorrupcionnye-videoteki-dlya-uchashihsya', videoteka, name='videoteka'),
        path('portfolio_of_links/<slug:slug>', LinksView.as_view(), name='links'),
        path('portfolio_of_links/', BagsView.as_view(), name='linksbag'),
        path('<slug:slug>', project, name='project'),
        path('', ProjectsList.as_view(), name='projects'),
    ])),
    path('about-us/', include([
        path('people/people_<int:id>', person, name='person'),
        path('people/', workers, name='structure'),
        path('', about, name='about'),
    ])),
    path('galleries/', include([
        path('<slug:slug>', gallery, name='gallery'),
        path('', GalleriesList.as_view(), name='galleries'),
    ])),
    path('user/', include([
        path('registration/', RegisterUser.as_view(), name='registration'),
        path('login/', LoginUser.as_view(), name='login'),
        path('logout/', logout_user, name='logout'),
        path('<str:username>', profile, name='profile')
    ])),
    path('search/', SearchList.as_view(), name='search'),
    path('contact/', contact_view, name='contact'),
    path('lastnews/', LatestFeedRSS(), name='rss'),
    path('', main, name='main'),
]
