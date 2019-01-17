from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from django.views import generic
from .models import Book
import json
import random

def index(request):
    return HttpResponse("Hello, you are at the bibs index.")

def randomBiblePassage(request):
    books = Book.objects.all()
    bookNum = random.randint(0, 65)
    book = books[bookNum].name
    maxChapters = random.randint(1, books[bookNum].numChapters)
    finalPassage = book + " " + str(maxChapters)
    dict = { "passage": finalPassage }
    return JsonResponse(dict)
