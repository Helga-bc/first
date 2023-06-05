from django.shortcuts import render
from .models import Book, Genre, Publisher
from django.http import HttpResponse


def books(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    publishers = Publisher.objects.all()
    return render(request, "index.html", context={"books": books,
                                                  "genres": genres,
                                                  "publishers": publishers})


def get_book(request, id):
    #.all - все
    #.get - один
    # .filter - фильтр
    # .create - создать
    # .delete - удалить
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse(f"<h1>Книги с  id {id} не существует</h1>")


    return render(request, "detail.html", context={"book":book})


def get_genre_books(request, title):
    try:
        genre = Genre.objects.get(title=title)
    except Genre.DoesNotExist:
        return HttpResponse(f"<h1>Жанра с таким названием не существует! </h1>")

    return render(request, "genre.html", context={"genre": genre})

