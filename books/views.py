from django.shortcuts import render
from .models import Book
from django.http import HttpResponse


def books(request):
    books = Book.objects.all()
    return render(request, "index.html", context={"books": books})
