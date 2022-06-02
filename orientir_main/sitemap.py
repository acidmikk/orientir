from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import News


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['main', 'contact', 'about']

    def location(self, item):
        return reverse(item)


class DynamicViewSitemap(Sitemap):

    def items(self):
        return News.objects.all()

    def location(self, item):
        # return reverse('news-page', args=[item.pk])
        return f'/news/{item.pk}/'
