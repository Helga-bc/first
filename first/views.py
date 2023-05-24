from django.http import HttpResponse


def first(request):
    return HttpResponse("<h1>Здесь будет сайт с книгами</h1>")


def second_func(request):
    return HttpResponse("<h1>Ольга</h1>")

def third_func(request):
    return HttpResponse("<h2>Сегодня хорошая погода<h2>")