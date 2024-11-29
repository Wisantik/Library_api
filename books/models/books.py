from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
from common.models.mixins import InfoMixin

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


class Book(InfoMixin):
    name = models.CharField(("Название книги"), max_length=255)
    date = models.DateField(("дата создания книги"),
                            auto_now=False, auto_now_add=False, null=True, blank=True)
    description = models.TextField(("Описание книги"))
    pages = models.IntegerField(("число страниц"))
    genres = models.ForeignKey(
        Genre, verbose_name=("Жанр"), on_delete=models.CASCADE)
    author = models.ManyToManyField(Author, verbose_name=("Автор книги"))
    rating = models.FloatField(_("рейтинг книги"))

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def update_rating(self):
        ratings = Rating.objects.filter(book=self)
        if ratings.exists():
            self.rating = ratings.aggregate(models.Avg('score'))['score__avg']
            self.save

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})


class comment(InfoMixin):
    # user = models.ForeignKey(User, verbose_name=_(
    #     "Пользователь"), on_delete=models.CASCADE) есть в INFO MIXIN
    text = models.TextField(("Текст комментария"))
    book = models.ForeignKey(Book,  related_name='comments', verbose_name=("для какой книги комент"),
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("comment")

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})


class Rating(InfoMixin):
    book = models.ForeignKey(Book, verbose_name=_(
        "рейтинг у книги"), on_delete=models.CASCADE, related_name='ratings')
    score = models.FloatField(_("рейтинг"))
    # user = models.ForeignKey(
    #     User, verbose_name=_("пользователь поставивший рейтинг"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Rating_detail", kwargs={"pk": self.pk})
