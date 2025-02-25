from django.db import models
from django.urls import reverse

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Article Category"
        verbose_name_plural = "Article Categories"


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='category'
    )
    created_on = models.DateTimeField(null=False)
    updated_on = models.DateTimeField(null=False)

    def __str__(self):
        return f"{self.title}; Cat: {self.category}"
    
    def get_absolute_url(self):
        return reverse("wiki:model_detail", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ["created_on"]
        verbose_name = "Article"
        verbose_name_plural = "Articles"
    
    