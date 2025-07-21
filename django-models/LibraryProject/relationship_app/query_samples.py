from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
    help = 'Sample queries for relationship_app models'

    def handle(self, *args, **kwargs):
        author = Author.objects.create(name="George Orwell")
        book1 = Book.objects.create(title="1984", author=author)
        book2 = Book.objects.create(title="Animal Farm", author=author)
        library = Library.objects.create(name="City Library")
        library.books.add(book1, book2)
        librarian = Librarian.objects.create(name="Jane Doe", library=library)

        print("Books by George Orwell:")
        books_by_author = Book.objects.filter(author__name="George Orwell")
        for book in books_by_author:
            print(f"- {book.title}")

        print("\nBooks in City Library:")
        books_in_library = Library.objects.get(name="City Library").books.all()
        for book in books_in_library:
            print(f"- {book.title}")

        print("\nLibrarian for City Library:")
        librarian = Librarian.objects.get(library__name="City Library")
        print(f"- {librarian.name}")