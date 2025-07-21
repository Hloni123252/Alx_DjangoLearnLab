from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
    help = 'Sample queries for relationship_app models'

    def handle(self, *args, **kwargs):
        # Create sample data
        author_name = "George Orwell"
        author = Author.objects.create(name=author_name)
        book1 = Book.objects.create(title="1984", author=author)
        book2 = Book.objects.create(title="Animal Farm", author=author)
        library_name = "City Library"
        library = Library.objects.create(name=library_name)
        library.books.add(book1, book2)
        librarian_name = "Jane Doe"
        librarian = Librarian.objects.create(name=librarian_name, library=library)

        # Query all books by a specific author
        print("Books by George Orwell:")
        books_by_author = Book.objects.filter(author__name=author_name)
        for book in books_by_author:
            print(f"- {book.title}")

        # List all books in a library
        print("\nBooks in a library:")
        specific_library = Library.objects.get(name=library_name)  # Explicit variable
        books_in_library = specific_library.books.all()
        for book in books_in_library:
            print(f"- {book.title}")

        # Retrieve the librarian for a library
        print("\nLibrarian for the library:")
        specific_librarian = Librarian.objects.get(library__name=library_name)
        print(f"- {specific_librarian.name}")