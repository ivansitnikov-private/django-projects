from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """ Функция-представление для теста отображения главной страницы"""
    return HttpResponse("Страница приложения women")

def categories(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Статьи по категориям</h1>")


