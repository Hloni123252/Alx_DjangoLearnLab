from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book', related_name='libraries')

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    library = models.OneToOneField('Library', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

