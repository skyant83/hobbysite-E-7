from django.db import models
from django.urls import reverse

from user_management.models import Profile


# Create your models here.
class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Thread category'
        verbose_name_plural = 'Thread categories'

    def __str__(self):
        return self.name


class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True)
    category = models.ForeignKey(
        ThreadCategory,
        on_delete=models.SET_NULL,
        null=True)
    entry = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/forum/', null=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return (f'{self.title}'
                f' created on {self.date_created.astimezone().ctime()}'
                f' last updated {self.date_updated.astimezone().ctime()}')

    def get_absolute_url(self):
        return reverse('forum:thread_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True)
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE)
    entry = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_created']
