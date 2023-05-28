from django.contrib import admin

from .models import Book, Genre, Movie, Category

# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)

admin.site.register(Movie)
admin.site.register(Category)
