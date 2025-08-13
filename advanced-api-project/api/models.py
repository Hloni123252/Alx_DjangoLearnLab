from django.db import models

# Model to store author information
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    # name: Stores the author's name, must be unique and cannot be null

    def __str__(self):
        return self.name

# Model to store book information with a relationship to Author
class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    # title: Stores the book's title, cannot be null
    publication_year = models.IntegerField(null=False)
    # publication_year: Stores the year the book was published, cannot be null
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    # author: Foreign key to Author, establishes a one-to-many relationship
    # (one author can have many books), on_delete.CASCADE deletes books if author is deleted

    def __str__(self):
        return f"{self.title} by {self.author.name}"