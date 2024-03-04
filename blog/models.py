from django.db import models
from django.contrib.auth.models import User


class post(models.Model) :
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),

    )
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body =models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("accounts/", include("django.contrib.auth.urls")),
    ]