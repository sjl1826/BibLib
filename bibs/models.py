from django.db import models

class Chapter(models.Model):
    chapter = models.CharField(max_length=10)

class Book(models.Model):
    name = models.CharField(max_length=30)
    chapters = models.ManyToManyField(Chapter)
