from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from itertools import chain
from .models import *


class LatestFeedRSS(Feed):
    title = "Новости фонда"
    link = ""
    description = 'Последние новости фонда "Рапир"'

    def items(self):
        query_sets = [News.objects.all()[:10],
                      Project.objects.all()[:10]]

        # и объединяем выдачу
        final_set = list(chain(*query_sets))[:10]
        final_set.sort(key=lambda x: x.published, reverse=True)
        return final_set

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)
