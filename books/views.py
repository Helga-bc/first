from django.shortcuts import render, redirect
from .models import Book, Genre, Publisher, Tag, Comment
from .forms import BookForm
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError


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
    if request.user.is_authenticated:
        if request.method == "GET":
            form = BookForm()
            return render(request, "add_book.html", context={"form": form})
        elif request.method == "POST":
            publisher_id = request.POST['publisher']
            genre_id = request.POST['genre']

            publisher = None
            genre = None
            image = request.FILES.get('image', 'no_image.png')

            if publisher_id != '':
                publisher = Publisher.objects.get(id=publisher_id)

            if genre_id != '':
                genre = Genre.objects.get(id=genre_id)

            book = Book.objects.create(title=request.POST['title'],
                                author=request.POST['author'],
                                year=request.POST['year'],
                                raiting=request.POST['raiting'],
                                publisher=publisher,
                                genre=genre,
                                image=image,
                                user=request.user)
            tags = request.POST.getlist('tags')
            book.tags.set(tags)
            book.save()

            return redirect("books")
    else:
        return HttpResponse("<h1>Только авторизованный пользователь может добавить книгу!</h1>")

    # if request.method == "GET":
    #     form = BookForm()
    #     return render(request, "add_book.html", context={"form": form})
    # elif request.method == "POST":
    #     form = BookForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         return HttpResponse("<h1>Что то пошло не так!</h1>")
    #
    # return redirect("books")


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

    title = request.GET["title"]
    genre = request.GET["genre"]
    price_lt = request.GET["price_lt"]

    books = Book.objects.all()
    result_string = "Результат поиска "

    if title != '':
        result_string += f"по названию : {title}  "
        books = books.filter(title__contains=title)
    if genre != '':
        result_string += f"по жанру : {genre}  "
        books = books.filter(genre__title__contains=genre)

    if price_lt != "":
        result_string += f"по цене : {price_lt}  "
        books = books.filter(price__lte=price_lt)

    # books = Book.objects.filter(title__contains=search_query)

    return render(request, "search_book.html", context={"books": books,
                                                        "result_string":result_string})


def delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse(f"<h1>Книги с  id {id} не существует</h1>")

    if request.user.username != book.user.username:
        return HttpResponse("<h1> У вас нет прав на удаление этой книги </h1>")
    else:
        book.delete()
        return redirect('books')





def update_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse(f"<h1>Книги с  id {id} не существует</h1>")

    if request.user.username != book.user.username:
        return HttpResponse("<h1> У вас нет прав на обновление этой книги </h1>")

    else:
        if request.method == "GET":
            form = BookForm(instance=book)
            return render(request, "update_book.html", context={"form": form,
                                                                "book": book})
        else:
            publisher_id = request.POST['publisher']
            genre_id = request.POST['genre']

            publisher = None
            genre = None
            image = request.FILES.get('image', 'no_image.png')

            if publisher_id != '':
                publisher = Publisher.objects.get(id=publisher_id)

            if genre_id != '':
                genre = Genre.objects.get(id=genre_id)

            book.title = request.POST['title']
            book.author = request.POST['author']
            book.year = request.POST['year']
            book.raiting = request.POST['raiting']
            book.publisher = publisher
            book.genre = genre
            book.image = image
            tags = request.POST.getlist('tags')
            book.tags.set(tags)

            book.save()

            return redirect("get_book", id=book.id)


def add_comment(request, id):
    if request.user.is_authenticated:
        try:
            book = Book.objects.get(id=id)
            raiting = 5
            try:
                Comment.objects.create(content=request.POST['comment'],
                                       raiting=raiting,
                                       user=request.user,
                                       book=book)
            except MultiValueDictKeyError:
                return HttpResponse("<h1> 404 </h1>")

            return redirect("get_book", id=id)
        except Book.DoesNotExist:
            return HttpResponse(f"<h1> книги с id {id} нет, вы не можете добавить комментарий! </h1>")
    else:
        return HttpResponse("<h1> Вы не авторизованы в системе! </h1>")


def buy_book(request, id):
    try:
        book = Book.objects.get(id=id)
        print(book.id)
    except Book.DoesNotExist:
        return HttpResponse(f"<h1> книги с id {id} не существует </h1>")

    if book.count != 0:
        book.count = book.count - 1
        book.save()
    else:
        return HttpResponse("<h1> 404 </h1>")

    return HttpResponse("<h1> страница покупки </h1>")
