from django.shortcuts import render

from goods.views import catalog

def login(request):
    context = {
        'title': 'Тепло в деталях - Авторизация'
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'Тепло в деталях - Регистрация'
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': 'Тепло в деталях - Кабинет'
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    ...
