from django.shortcuts import render
from django.http import HttpResponse

def books(request):
    return HttpResponse("Список книг")

def movies(request):
    return HttpResponse("Список фильмов")
