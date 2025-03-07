from django.contrib import admin
from .models import Article, ArticleCategory


class ArticleInline(admin.TabularInline):
    model = Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInline,]


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ("title", "category",)
    list_display = ("title", "created_on", "updated_on")
    list_filter = ("title", "category", "created_on", "updated_on")
    fieldsets = (
        ("Article Information", {
            "fields": [
                ("title", "category",),
                "entry"
            ]
        }),
    )


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
