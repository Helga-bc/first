from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, PostTag
from .forms import PostForm, PostTagForm, PostCategory, PostCategoryForm


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
        category_id = request.POST['category']


        category = None
        image = None

        if category != '':
            category = PostCategory.objects.get(id=category_id)

        if request.FILES['image'] != '':
            image = request.FILES['image']

        post = Post.objects.create(title=request.POST['title'],
                                   description=request.POST['description'],
                                   category=category,
                                   image=image)
        tags = request.POST.getlist('tags')
        post.tags.set(tags)
        post.save()

        return redirect("posts")





    #
    # # переписсать функцию, эта не добавляет картинку
    # if request.method == "GET":
    #     form = PostForm()
    #     return render(request, "add_post.html", context={"form": form})
    # elif request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         return HttpResponse("<h1>Что то пошло не так!</h1>")
    #
    # return HttpResponse("<h2>Пост добавлен !</h2>")
    #

def search_post(request):
    title = request.GET['title']
    category = request.GET["category"]

    posts = Post.objects.all()

    if title != '':
        posts = posts.filter(title__contains=title)
    if category != '':
        posts = posts.filter(category__title__contains=category)

    return render(request, "search_post.html", context={"posts": posts})



def delete_post(request, id):
    try:
        post = Post.objects.get(id=id)

    except Post.DoesNotExist:
        return HttpResponse(f"<h1> Поста с id {id} не существует</h1>")
    post.delete()
    return redirect('posts')
