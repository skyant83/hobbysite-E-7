from django.contrib import admin
from .models import Article, ArticleCategory, Comment


class ArticleInline(admin.TabularInline):
    model = Article


class CommentInline(admin.TabularInline):
    model = Comment


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    fieldsets = (
        ('Comments', {
            "fields": (
                "author",
                "entry"
            ),
        }),
    )


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInline,]


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [CommentInline,]
    search_fields = ("title", "category",)
    list_display = ("title", "created_on", "updated_on")
    list_filter = ("title", "category", "created_on", "updated_on")
    fieldsets = (
        ("Article Information", {
            "fields": [
                ("title", "author", "category",),
                "entry"
            ]
        }),
    )


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
