from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(("название жанра"), max_length=50)
    description = models.TextField(("Описание Жанра"))
    date = models.DateField(("дата создания жанра"),
                            auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = ("Genre")
        verbose_name_plural = ("Genres")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Genre_detail", kwargs={"pk": self.pk})


class Author(models.Model):
    name = models.CharField(("Имя автора"), max_length=50,)
    date = models.DateField(
        'дата рождения', auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = ("Authors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})


class Book(models.Model):
    name = models.CharField(("Название книги"), max_length=255)
    date = models.DateField(("дата создания книги"),
                            auto_now=False, auto_now_add=False, null=True, blank=True)
    description = models.TextField(("Описание книги"))
    pages = models.IntegerField(("число страниц"))
    genres = models.ForeignKey(
        Genre, verbose_name=("Жанр"), on_delete=models.CASCADE)
    author = models.ManyToManyField(Author, verbose_name=("Автор книги"))

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})


class comment(models.Model):
    User = models.ForeignKey(User, verbose_name=(
        "создатель комента"), on_delete=models.CASCADE)
    date = models.DateField(("Дата создания комментария"),
                            auto_now=False, auto_now_add=False)
    text = models.TextField(("Текст комментария"))
    book = models.ForeignKey(Book, verbose_name=("для какой книги комент"),
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("comment")

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})
