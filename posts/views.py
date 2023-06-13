from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, PostTag
from .forms import PostForm, PostTagForm


def posts(request):
    posts = Post.objects.all()
    tags = PostTag.objects.all()
    return render(request, "index_posts.html", context={"posts": posts,
                                                        "tags": tags})


def get_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return HttpResponse(f"<h1>Пост с  id {id} не существует</h1>")
    return render(request, "post_detail.html", context={"post": post})


def get_tag_post(request, title):
    try:
        tag = PostTag.objects.get(title=title)
    except PostTag.DoesNotExist:
        return HttpResponse(f"<h1>Тэг с таким названием {title} не найден! </h1>")

    return render(request, "tag_info.html", context={"tag": tag,
                                                     "title": title})


def add_post_tag(request):
    form = PostTagForm()
    return render(request, "add_PostTag.html", context={"form": form})


def create_post_tag(request):
    PostTag.objects.create(title=request.POST['title'])
    return HttpResponse("<h2>Сохранено!</h2>")


def add_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "add_post.html", context={"form": form})
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("<h1>Что то пошло не так!</h1>")

    return HttpResponse("<h2>Пост добавлен !</h2>")



def search_post(request):
    search_query = request.GET['search']
    posts = Post.objects.filter(title__contains=search_query)
    return render(request, "search_post.html", context={"posts": posts})

