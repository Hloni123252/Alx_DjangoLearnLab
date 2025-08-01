from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    text = '\n'.join(f"{book.title} by {book.author.name}" for book in books)
    return HttpResponse(text)

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Optional template is fine here
    context_object_name = 'library'