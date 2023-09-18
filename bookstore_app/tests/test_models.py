from django.test import TestCase
from bookstore_app.models import Author, Category, Book

class BookstoreModelTests(TestCase):
    def setUp(self):
        # Create some test data for your models
        self.category = Category.objects.create(name='Test Category')
        self.author = Author.objects.create(name='Test Author', biography='Test Biography')
        self.book = Book.objects.create(
            title='Test Book',
            description='Test Description',
            price=10.99,
            publication_date='2023-01-01',
            author=self.author,
            category=self.category,
        )

    def test_category_creation(self):
        # Test if a category was created successfully
        self.assertEqual(self.category.name, 'Test Category')

    def test_author_creation(self):
        # Test if an author was created successfully
        self.assertEqual(self.author.name, 'Test Author')
        self.assertEqual(self.author.biography, 'Test Biography')

    def test_book_creation(self):
        # Test if a book was created successfully
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.description, 'Test Description')
        self.assertEqual(self.book.price, 10.99)
        self.assertEqual(str(self.book.publication_date), '2023-01-01')
        self.assertEqual(self.book.author, self.author)
        self.assertEqual(self.book.category, self.category)

    