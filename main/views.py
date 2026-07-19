from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Тепло в деталях - Главная',
        'content': 'Магазин ручных товаров "Тепло в деталях"'
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Тепло в деталях - О нас',
        'content': 'О нас',
        'text_on_page': 'Мы правда крутые, купите свечку'
    }    
    return render(request, 'main/about.html', context)