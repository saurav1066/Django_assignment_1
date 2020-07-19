from django.contrib import admin

from .models import Author, Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'date_posted', 'author')
    ordering = ('date_posted',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

