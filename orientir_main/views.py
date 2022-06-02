from itertools import chain
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.generic import ListView
from django.conf import settings

from .models import *
from .forms import ContactForm


class NewsList(ListView):
    model = News
    queryset = News.objects.all()
    template_name = 'orientir_main/news.html'
    paginate_by = 12


def new(request, slug):
    cur_new = News.objects.get(slug=slug)
    context = {'new': cur_new}
    return render(request, 'orientir_main/new.html', context)


class ProjectsList(ListView):
    model = Project
    queryset = Project.objects.all()
    template_name = 'orientir_main/searches.html'
    paginate_by = 12


def project(request, slug):
    cur_exploration = Project.objects.get(slug=slug)
    context = {'project': cur_exploration}
    return render(request, 'orientir_main/search.html', context)


def main(request):
    last_news = News.objects.all()[:3]
    last_project = Project.objects.all()[:2]
    list_people = People.objects.all()
    slider = Slider.objects.all()

    context = {'last_news': last_news,
               'projects': last_project,
               'experts': list_people,
               'slider': slider}
    return render(request, 'orientir_main/index.html', context)


def workers(request):
    list_worker = People.objects.all()
    context = {'experts': list_worker}
    return render(request, 'orientir_main/experts.html', context)


def about(request):
    list_worker = People.objects.all()
    other = About.objects.first()
    context = {'experts': list_worker,
               'about': other}
    return render(request, 'orientir_main/about.html', context)


class GalleriesList(ListView):
    model = Album
    queryset = Album.objects.all()
    template_name = 'orientir_main/galleries.html'
    paginate_by = 12

def gallery(request, slug):
    gal_lery = Photo.objects.filter(album__slug=slug)
    title = Album.objects.get(slug=slug)
    context = {'gallery': gal_lery,
               'album': title}
    return render(request, 'orientir_main/gallery.html', context)


class SmiList(ListView):
    model = Smi
    queryset = Smi.objects.all()
    template_name = 'orientir_main/mass_media.html'
    paginate_by = 12


class SearchList(ListView):
    template_name = 'orientir_main/search_result.html'
    paginate_by = 12

    def get_queryset(self):
        query_sets = []
        q = self.request.GET.get('q')
        query_sets.append(News.objects.search(query=q))
        query_sets.append(Project.objects.search(query=q))

        # и объединяем выдачу
        final_set = list(chain(*query_sets))
        final_set.sort(key=lambda x: x.published, reverse=True)
        return final_set

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['mess']
            recepients = [settings.EMAIL_HOST_USER]
            send_mail(name + ' -- ' + email, message, settings.EMAIL_HOST_USER, recepients)
            return redirect('main')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'orientir_main/contact.html', {'form': form})