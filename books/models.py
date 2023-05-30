from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"Тэг: {self.title}"

class Publisher(models.Model):
    LANGUAGES = (
        ("ru", "Russian"),
        ("en", "English"),
        ("fr", "French")
    )

    title = models.CharField(max_length=50)
    language = models.CharField(max_length=2, choices=LANGUAGES, default="ru")

    def __str__(self):
        return f"Издание: {self.title} {self.language}"

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField(blank=True)
    raiting = models.IntegerField(default=0)

    genre = models.ForeignKey("Genre", on_delete=models.DO_NOTHING, null=True, blank=True, related_name='books')
    tags = models.ManyToManyField("Tag", related_name="books")

    publisher = models.OneToOneField("Publisher", on_delete=models.DO_NOTHING, default=None)

    def __str__(self):
        return f"Книга:{self.id} Название: {self.title} Автор: {self.author}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"Жанр {self.id}: {self.title}"

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    movie_year = models.IntegerField(null=True, blank=True)
    movie_director = models.CharField(max_length=50, null=True, blank=True)
    movie_description = models.CharField(max_length=500, null=True, blank=True)
    category_name = models.ForeignKey("Category", on_delete=models.DO_NOTHING, null=True, blank=True, related_name='movies')

    def __str__(self):
        return f"{self.id}. Фильм: {self.movie_name}, год {self.movie_year}, " \
               f"Режиссер {self.movie_director}, Описание {self.movie_description}"

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}. {self.category_name}"
