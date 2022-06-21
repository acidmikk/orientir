from itertools import chain

from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.conf import settings

from .models import *
from .forms import ContactForm


class NewsList(ListView):
    model = News
    queryset = News.objects.all()
    context_object_name = 'news'
    template_name = 'orientir_main/news.html'
    paginate_by = 12


def new(request, slug):
    cur_new = News.objects.get(slug=slug)
    context = {'new': cur_new}
    return render(request, 'orientir_main/new.html', context)


class ProjectsList(ListView):
    model = Project
    queryset = Project.objects.all()
    context_object_name = 'projects'
    template_name = 'orientir_main/projects.html'
    paginate_by = 12


def project(request, slug):
    cur_project = Project.objects.get(slug=slug)
    context = {'project': cur_project}
    return render(request, 'orientir_main/project.html', context)


def main(request):
    last_news = News.objects.all()[:3]
    last_project = Project.objects.all()[:2]
    list_people = People.objects.all()
    slider = Slider.objects.all()
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

    context = {'last_news': last_news,
               'projects': last_project,
               'experts': list_people,
               'slider': slider,
               'form': form}
    return render(request, 'orientir_main/index.html', context)


def workers(request):
    list_worker = People.objects.all()
    context = {'experts': list_worker}
    return render(request, 'orientir_main/experts.html', context)


def person(request, id):
    worker = People.objects.get(id=id)
    context = {'expert': worker}
    return render(request, 'orientir_main/expert.html', context)


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


def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:
        username:     {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff:     {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active:    {request.user.is_active}
    """
    return HttpResponse(text, content_type="text/plain")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'orientir_main/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main:main')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'orientir_main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('main:main')


def logout_user(request):
    logout(request)
    return redirect('main:login')


@login_required
def profile(request, username):
    return render(request, 'orientir_main/lk.html', {'user': User.objects.get(username=username)})
