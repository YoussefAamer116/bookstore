from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    Model for book categories.

    Attributes:
        name (str): The name of the category.
    """
    name = models.CharField(max_length=100)

class Author(models.Model):
    """
    Model for book authors.

    Attributes:
        name (str): The name of the author.
        biography (str): The biography of the author.
    """
    name = models.CharField(max_length=100)
    biography = models.TextField()

class Book(models.Model):
    """
    Model for books.

    Attributes:
        title (str): The title of the book.
        description (str): A description of the book.
        price (Decimal): The price of the book.
        publication_date (Date): The publication date of the book.
        author (Author): The author of the book (foreign key to Author model).
        category (Category): The category of the book (foreign key to Category model).
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
