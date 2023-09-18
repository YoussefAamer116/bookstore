from django.test import TestCase
from django.contrib.auth.models import User
from bookstore_app.models import Author, Category, Book
from bookstore_app.serializers import AuthorSerializer, CategorySerializer, BookSerializer

class AuthorSerializerTest(TestCase):
    def test_author_serializer(self):
        author_data = {'name': 'Test Author', 'biography': 'Test Biography'}
        serializer = AuthorSerializer(data=author_data)
        self.assertTrue(serializer.is_valid())


class CategorySerializerTest(TestCase):
    def test_category_serializer(self):
        category_data = {'name': 'Test Category'}
        serializer = CategorySerializer(data=category_data)
        self.assertTrue(serializer.is_valid())


class BookSerializerTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author', biography='Test Biography')
        self.category = Category.objects.create(name='Test Category')

    def test_book_serializer(self):
        book_data = {
            'title': 'Test Book',
            'description': 'Test Description',
            'price': '10.99',
            'publication_date': '2023-01-01',
            'author': self.author.id,
            'category': self.category.id,
        }
        serializer = BookSerializer(data=book_data)
        self.assertTrue(serializer.is_valid())


