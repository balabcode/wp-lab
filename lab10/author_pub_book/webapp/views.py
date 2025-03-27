from django.shortcuts import render, redirect
from .forms import AuthorForm, PublisherForm, BookForm
from .models import Author, Publisher, Book

def main(request):
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    books = Book.objects.all()

    if request.method == 'POST':
        author_form = AuthorForm(request.POST, prefix='author')
        publisher_form = PublisherForm(request.POST, prefix='publisher')
        book_form = BookForm(request.POST, prefix='book')

        if author_form.is_valid():
            author_form.save()
            return redirect('main')

        if publisher_form.is_valid():
            publisher_form.save()
            return redirect('main')

        if book_form.is_valid():
            book_form.save()
            return redirect('main')

    else:
        author_form = AuthorForm(prefix='author')
        publisher_form = PublisherForm(prefix='publisher')
        book_form = BookForm(prefix='book')

    context = {
        'authors': authors,
        'publishers': publishers,
        'books': books,
        'author_form': author_form,
        'publisher_form': publisher_form,
        'book_form': book_form,
    }
    return render(request, 'main.html', context)