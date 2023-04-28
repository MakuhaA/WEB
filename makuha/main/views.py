from django.shortcuts import render
from django.http import HttpReponse


def index(request):
    return HttpReponse("<h4>Проверка работы</h4>")


def about(request):
    return HttpReponse("<h4>Про нас</h4>")
