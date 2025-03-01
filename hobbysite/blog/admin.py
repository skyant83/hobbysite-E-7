from django.contrib import admin

from .models import Article, ArticleCategory

# Register your models here.


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ('title',)
    list_display = ('title', 'category', 'created_on', 'updated_on',)
    list_filter = ('title', 'category', 'created_on', 'updated_on',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
