from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def index(request):
    return HttpResponse("<h2>Главная<h2/>")


def about(request):
    return HttpResponse("<h2>About<h2/>")


def contact(request):
    return HttpResponseRedirect('/about')


def products(request, product_id=1):
    category = request.GET.get('cat', '')
    output = f"<h2>Продукт №{product_id} Категория: {category}<h2/>"
    return HttpResponse(output)


def users(request):
    id = request.GET.get('id', 1)
    name = request.GET.get('name', 'Максим')
    output = f"<h2>Пользователь<h2/>" \
             f"<h3>id: {id} Имя: {name}<h3/>"
    return HttpResponse(output)


def details(request):
    return HttpResponsePermanentRedirect('/')
