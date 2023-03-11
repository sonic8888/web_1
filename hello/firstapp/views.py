from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse


def index(request):
    # header = "Персональные данные"  # обычная переменная
    # langs = ["Английский", "Немецкий", "Испанский"]  # массив
    # user = {"name": "Максим,", "age": 30}  # словарь
    # addr = ("Виноградная", 23, 45)  # кортеж
    # data = {"header": header, "langs": langs, "user": user, "address": addr}
    return TemplateResponse(request, "firstapp\\home.html")


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
