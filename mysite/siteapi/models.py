
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Site(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sites')
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='pages')
    title = models.CharField(max_length=255)
    html_content = models.TextField()
    css_content = models.TextField(blank=True)
    js_content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title