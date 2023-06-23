from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(default=None, blank=True)
    tags = models.ManyToManyField("PostTag", related_name="posts")
    date_create = models.DateField(null=True, blank=True, default=None)

    category = models.ForeignKey("PostCategory", on_delete=models.SET_NULL,
                                 null=True, blank=True, related_name='post_category'
                                 )

    image = models.ImageField(default='no_image.png')


    def __str__(self):
        return f"{self.id}. Пост: {self.title}, {self.description}" \
               f", {self.category}, {self.date_create}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class PostTag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} Тэг: {self.title}"

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class PostCategory(models.Model):

    title = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.id}. Категория: {self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

