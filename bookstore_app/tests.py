from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import Author, Category, Book

class BookAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create authors and categories as needed for your tests
        self.author = Author.objects.create(name='Test Author')
        self.category = Category.objects.create(name='Test Category')

    def test_authenticated_create_book(self):
        response = self.client.post('/api/books/', {
            'title': 'Test Book',
            'description': 'Test description',
            'price': 19.99,
            'publication_date': '2023-08-10',
            'author': self.author.id,  # Use the correct author ID
            'category': self.category.id,  # Use the correct category ID
        })
        self.assertEqual(response.status_code, 201)  # 201 indicates created

    def test_unauthenticated_create_book(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/books/', {})
        self.assertEqual(response.status_code, 401)  # 401 indicates unauthorized

    # Add more test cases as needed
