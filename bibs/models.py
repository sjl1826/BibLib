from django.db import models

class Passage(models.Model):
    book = models.CharField(max_length=30)
    chapter = models.CharField(max_length=10)
