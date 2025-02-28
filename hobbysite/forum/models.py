from datetime import datetime

from django.db import models
from django.urls import reverse


# Create your models here.
class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}\n\n{self.description}'


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        PostCategory,
        on_delete = models.SET_NULL,
        null = True)
    entry = models.TextField()
    date_created = models.DateTimeField(datetime.now())
    date_updated = models.DateTimeField()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.title} created on {self.date_created} last updated {self.date_updated}'
    
    def get_absolute_url(self):
        return reverse('forum:post', kwargs={'pk': self.pk})
    
    def save(self, **kwargs):
        self.date_updated = datetime.now()