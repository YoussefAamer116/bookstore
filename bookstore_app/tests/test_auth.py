#this test is for authentication and permissions

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
#from bookstore_app.models import Book  

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_unauthenticated_create_book(self):
        response = self.client.post('/api/books/', {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_create_book(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

        response = self.client.post('/api/books/', {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
