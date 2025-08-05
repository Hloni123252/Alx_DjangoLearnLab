from .models import Book

def run():
    Book.objects.create(title="Django for Beginners", author="William S. Vincent")
    Book.objects.create(title="REST APIs with Django", author="John Doe")
    print("Books seeded successfully!")

if __name__ == "__main__":
    run()