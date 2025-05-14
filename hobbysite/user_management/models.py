from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=63, unique=True)
    email_address = models.EmailField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse("user_management:profile_update",
                       kwargs={"slug": self.slug})
