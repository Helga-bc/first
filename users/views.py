from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, LoginUserForm
from django.contrib.auth.models import User
import django
from django.contrib.auth import authenticate, login, logout


def register_user(request):
    if request.method == 'GET':
        form = UserForm()

        return render(request, "register.html", context={"form": form})

    else:
        email = request.POST["email"]
        if User.objects.filter(email=email).count() != 0:
            return HttpResponse("<h1> Пользователь с таким email уже существует</h1>")
        else:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                 email=email)
            except django.db.utils.IntegrityError:
                return HttpResponse("<h1> Пользователь с таким логином уже существует</h1>")
            user.set_password(request.POST['password'])
            user.save()
            return HttpResponse("<h1>Вы успешно зарегистрировались</h1>")


def login_user(request):
    if request.method == 'GET':
        form = LoginUserForm()
        return render(request, 'login_user.html', context={"form": form})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # print(user) если логин и пароль верные то вернет пользователя
        # в обратном случае вернет None

        # form = LoginUserForm()
        # if user is not None:
        #     return HttpResponse("<h1>Логин и пароль верный, вы можете войти</h1>")
        # else:
        #     return HttpResponse("<h1>Проверьте правильность логина и пароля</h1>")
        # return render(request, 'login_user.html', context={"form": form})

        if user is not None:
            login(request, user=user)
        else:
            return HttpResponse("<h1> Что-то пошло не так!</h1>")

        return redirect('books')


def logout_user(request):
    logout(request)
    return redirect('books')