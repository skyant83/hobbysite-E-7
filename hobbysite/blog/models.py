from django.db import models
from django.urls import reverse

# Create your models here.


class ArticleCategory(models.Model):
    '''Model definition for ArticleCategory.'''

    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        '''Meta definition for ArticleCategory.'''

        ordering = ['name']
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'


class Article(models.Model):
    '''Model definition for Article.'''

    title = models.CharField(max_length=255, verbose_name='Article Title')
    category = models.ForeignKey(
                        ArticleCategory,
                        on_delete=models.SET_NULL,
                        null=True,
                        verbose_name='Category')
    entry = models.TextField()
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
        '''Meta definition for Article.'''

        ordering = ['-created_on']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
