from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Войти', 'url_name': 'login'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        ]
data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
    ]

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """ Функция-представление для теста отображения главной страницы"""
    

    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    
    #  t = render_to_string('women/index.html')
    return render(request, 'women/index.html', context=data)

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'women/about.html')

def show_post(request: HttpRequest , post_id: int) -> HttpResponse:
    return HttpResponse(f'Отображение статьи с id = {post_id}')

def page_not_found(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
