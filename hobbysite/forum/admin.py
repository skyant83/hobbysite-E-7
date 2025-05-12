from django.contrib import admin

from .models import ThreadCategory, Thread, Comment


# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment


class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory


class ThreadAdmin(admin.ModelAdmin):
    model = Thread
    inlines = [CommentInline,]


class CommentAdmin(admin.ModelAdmin):
    model = Comment


admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)
