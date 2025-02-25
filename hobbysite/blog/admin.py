from django.contrib import admin

from .models import Article, ArticleCategory

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    readonly_fields = ('created_on', 'updated_on')
    fieldsets = [
        ('Details', {
                'fields': [
                    'title', 'category', ('created_on', 'updated_on'), 'entry'
                ]
        }),
    ]


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
