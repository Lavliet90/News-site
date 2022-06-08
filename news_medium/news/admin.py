from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Article, Comment, CategoryArticle


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug_field', 'photo', 'get_html_photo', 'status')
    list_filter = ('author', 'status', 'last_change', 'create')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug_field': ('title',)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width = 50>")

    get_html_photo.short_description = 'Photo'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'article', 'comment_create')
    list_filter = ('comment_create',)
    search_fields = ('name', 'email', 'body')


class CategoryArticleAdmin(admin.ModelAdmin):
    list_filter = ('create',)
    list_display = ('name_category', 'slug', 'create')
    prepopulated_fields = {'slug': ('name_category',)}


admin.site.register(CategoryArticle, CategoryArticleAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
