from datetime import datetime

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateTimeField(default= datetime.now, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

