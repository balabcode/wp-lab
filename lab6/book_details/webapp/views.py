# webapp/views.py
from django.shortcuts import render, get_object_or_404
from .models import Book

def home(request):
    book = Book.objects.first()  # Get the first book (MVP)
    return render(request, 'webapp/home.html', {'book': book})

def metadata(request):
    book = Book.objects.first()
    return render(request, 'webapp/metadata.html', {'book': book})

def reviews(request):
    book = Book.objects.first()
    return render(request, 'webapp/reviews.html', {'book': book})

def publisher_info(request):
    book = Book.objects.first()
    return render(request, 'webapp/publisher_info.html', {'book': book})