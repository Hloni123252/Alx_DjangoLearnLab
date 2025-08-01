from django.shortcuts import render
from django.views.generic import DetailView
from relationship_app.models import Book, Library

# Function-based View 
def book_list(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-based View 
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'