from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout

from django.contrib import messages

from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегистрировались.")
            return redirect('home')
        else:
            messages.error(request, "Ошибка регистрации.")
    else:
        form = UserRegisterForm()

    return render(request, 'news/register.html', {"form" : form})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {"form" : form})

def user_logout(request):
    logout(request)
    return redirect("home")


class HomeNews(ListView):
    paginate_by = 10
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Main Page'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    paginate_by = 2
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewSingleNews(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news_item"


class CreateNews(LoginRequiredMixin,CreateView):
    form_class = NewsForm
    template_name = "news/add_news.html"
    raise_exception = True
