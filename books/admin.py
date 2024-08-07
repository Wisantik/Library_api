from typing import Any
from django.contrib import admin
from django.db.models import Count
from django.http import HttpRequest
from django.urls import reverse
import books
from books.models.books import Book, Genre, Author, comment
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pages', 'genres', 'authors_count')
    list_filter = ('author',)
    search_fields = ('name',)
    # readonly_fields = ('pages',)  # обычно для crated by и подобных
    autocomplete_fields = ('author',)
    filter_horizontal = ('author',)
    # так можно сделать чтобы ваабще не все можно было нажать
    list_display_links = list_display

    def authors_count(self, obj):
        # x = obj.author.count()  # обращается к объекту из строчки в админке(к каждому по своему)
        # return f'{x}'
        return obj.authors_count

    authors_count.short_description = 'количество авторов'

    def get_queryset(self, request):
        queryset = Book.objects.annotate(
            authors_count=Count('author__id')
        )
        return queryset


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(comment)
class сommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_link', 'User',)
    list_filter = ('book__pages',)  # заходим вглубь объекта

    def book_link(self, obj):
        link = reverse(
            'admin:books_book_change', args=[obj.book.id]
        )
        return format_html('<a href="{}">{}</a>', link, obj.book)
