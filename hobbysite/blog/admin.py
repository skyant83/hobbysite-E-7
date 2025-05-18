from django.contrib import admin

from .models import Article, ArticleCategory, Comment

# Register your models here.


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ('title',)
    list_display = ('title', 'category', 'created_on', 'updated_on',)
    list_filter = ('title', 'category', 'created_on', 'updated_on',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Comment'''

    search_fields = ('author', 'entry',)
    list_display = ('author', 'entry', 'article', 'created_on', 'updated_on',)
    list_filter = ('author', 'article', 'created_on', 'updated_on',)
    ordering = ('-created_on',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
