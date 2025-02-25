from django.db import models

# Create your models here.


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    # inlines = [Artr]

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
                        ArticleCategory,
                        on_delete=models.SET_NULL,
                        null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    entry = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']
