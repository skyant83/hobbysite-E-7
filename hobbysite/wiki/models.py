from django.db import models
from django.urls import reverse
from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'


class Article(models.Model):
    title = models.CharField(max_length=255)
    entry = models.TextField(null=True)
    header_image = models.ImageField(
        null=True,
        upload_to='images/'
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='article_author'
    )
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='category'
    )
    created_on = models.DateTimeField(
        null=False,
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        null=False,
        auto_now=True
    )

    def __str__(self):
        return f'{self.title} by {self.author}'

    def get_absolute_url(self):
        return reverse('wiki:article_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['created_on']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comment(models.Model):
    entry = models.TextField()
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='comment_author'
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='article'
    )
    created_on = models.DateTimeField(
        null=False,
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        null=False,
        auto_now=True
    )

    def __str__(self):
        return f"{self.author}'s comment on {self.article}."

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
