from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """ Функция-представление для теста отображения главной страницы"""
    #  t = render_to_string('women/index.html')
    return render(request, 'women/index.html')


def categories(request: HttpRequest, cat_id: int) -> HttpResponse:
    return HttpResponse(f"<h1>Статьи по категориям</h1><p> id {cat_id}</p>")
 
def categories_by_slug(request: HttpRequest, cat_slug: str) -> HttpResponse:
    if request.GET:
        print(f"Словарь {request.GET}")
    return HttpResponse(f"<h1>Статьи по категориям</h1><p> slug {cat_slug}  {request.GET}</p>")

def archive(request: HttpRequest, year) -> HttpResponse:
    if year > 2023: 
       return redirect('home')
    return HttpResponse(f"<h1>Архив</h1><p> year {year} </p>")

def page_not_found(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
