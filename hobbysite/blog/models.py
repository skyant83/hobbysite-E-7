from django.db import models
from django.urls import reverse

from user_management.models import Profile

# Create your models here.


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Article Title')
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='author'
    )
    category = models.ForeignKey(
                        ArticleCategory,
                        on_delete=models.SET_NULL,
                        null=True,
                        verbose_name='Category')
    entry = models.TextField()

    header_image = models.ImageField(
        null=True,
        upload_to='images/blog/',
        verbose_name='header_image'
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Dated Created')
    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name='Last Updated')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comment(models.Model):
    '''Model definition for Comment.'''
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    entry = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Dated Created')
    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name='Last Updated')

    def __str__(self):
        return f'Comment in {self.article.title} by {self.author}'

    class Meta:
        '''Meta definition for Comment.'''
        ordering = ['created_on']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
