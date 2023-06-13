from django.shortcuts import render, redirect
from .models import Book, Genre, Publisher, Tag
from .forms import BookForm
from django.http import HttpResponse


def books(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    publishers = Publisher.objects.all()
    return render(request, "index.html", context={"books": books,
                                                  "genres": genres,
                                                  "publishers": publishers})


def get_book(request, id):
    # .all - все
    # .get - один
    # .filter - фильтр
    # .create - создать
    # .delete - удалить
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse(f"<h1>Книги с  id {id} не существует</h1>")

    return render(request, "detail.html", context={"book": book})


def get_genre_books(request, title):
    try:
        genre = Genre.objects.get(title=title)
    except Genre.DoesNotExist:
        return HttpResponse(f"<h1>Жанра с таким названием не существует! </h1>")

    return render(request, "genre.html", context={"genre": genre})


def get_tag_books(request, title):
    try:
        tag = Tag.objects.get(title=title)
    except Tag.DoesNotExist:
        return HttpResponse(f"<h1>Тэга с таким названием {title} не существует! </h1>")

    tag_books = tag.books.all()
    return render(request, "tag_detail.html", context={"tag_books": tag_books,
                                                       "tag": tag})


def add_book(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, "add_book.html", context={"form": form})
    elif request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("<h1>Что то пошло не так!</h1>")

    return redirect("books")


        # publisher_id = request.POST["publisher"]
        # genre_id = request.POST["genre"]
        #
        # if publisher_id != '' and genre_id != '':
        #     publisher = Publisher.objects.get(id=publisher_id)
        #     genre = Genre.objects.get(id=genre_id)
        #
        # else:
        #     publisher = None
        #     genre = None
        #
        # book = Book(title=request.POST['title'],
        #             author=request.POST['author'],
        #             year=request.POST['year'],
        #             raiting=request.POST['raiting'],
        #             publisher=publisher,
        #             genre=genre)
        # book.save()
        # tags = request.POST.getlist('tags')
        # book.tags.set(tags)
        # book.save()
        # form = BookForm()
        # return render(request, "add_book.html", context={"form": form})







# def create_book(request):
#     genre = Genre.objects.get(id=request.POST['genre'])
#
#     Book.objects.create(title=request.POST['title'],
#                         author=request.POST['author'],
#                         year=request.POST['year'],
#                         # tags=request.POST['tags'],
#                         raiting=request.POST['raiting'],
#                         # publisher=request.POST['publisher'],
#                         genre=genre
#                         )
#     return HttpResponse("<h1> Получилось! </h1>")


def search_book(request):
    search_query = request.GET['search']
    books = Book.objects.filter(title__contains=search_query)
    return render(request, "search_book.html", context={"books": books})
