from django.contrib import admin

from .models import ThreadCategory, Thread


# Register your models here.
class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory


class PostAdmin(admin.ModelAdmin):
    model = Thread


admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, PostAdmin)
