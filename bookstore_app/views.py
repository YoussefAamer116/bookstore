from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.shortcuts import render
from .models import Book, Author, Category
from .serializers import BookSerializer, AuthorSerializer, CategorySerializer, UserSerializer
from django.contrib.auth.views import LoginView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: AuthorSerializer(many=True),
            status.HTTP_201_CREATED: AuthorSerializer(),
            status.HTTP_400_BAD_REQUEST: "Bad Request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_403_FORBIDDEN: "Forbidden",
            status.HTTP_404_NOT_FOUND: "Not Found",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Internal Server Error",
        },
        operation_description="API endpoint that allows authors to be viewed or edited",
    )
    def list(self, request, *args, **kwargs):
        """
        List all authors.
        """
        return super().list(request, *args, **kwargs)

    # Define similar @swagger_auto_schema decorators for other methods (create, retrieve, update, destroy)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: CategorySerializer(many=True),
            status.HTTP_201_CREATED: CategorySerializer(),
            status.HTTP_400_BAD_REQUEST: "Bad Request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_403_FORBIDDEN: "Forbidden",
            status.HTTP_404_NOT_FOUND: "Not Found",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Internal Server Error",
        },
        operation_description="API endpoint that allows categories to be viewed or edited",
    )
    def list(self, request, *args, **kwargs):
        """
        List all categories.
        """
        return super().list(request, *args, **kwargs)

    # Define similar @swagger_auto_schema decorators for other methods (create, retrieve, update, destroy)

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ['category__name', 'author__name']
    search_fields = ['title', 'description']

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: BookSerializer(many=True),
            status.HTTP_201_CREATED: BookSerializer(),
            status.HTTP_400_BAD_REQUEST: "Bad Request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_403_FORBIDDEN: "Forbidden",
            status.HTTP_404_NOT_FOUND: "Not Found",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Internal Server Error",
        },
        operation_description="API endpoint that allows books to be viewed or edited",
    )
    def list(self, request, *args, **kwargs):
        """
        List all books with pagination and filtering.
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=BookSerializer,
        responses={
            status.HTTP_201_CREATED: BookSerializer(),
            status.HTTP_400_BAD_REQUEST: "Bad Request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_403_FORBIDDEN: "Forbidden",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Internal Server Error",
        },
        operation_description="Create a new book",
    )
    def create(self, request, *args, **kwargs):
        """
        Create a new book.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: BookSerializer(),
            status.HTTP_400_BAD_REQUEST: "Bad Request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_403_FORBIDDEN: "Forbidden",
            status.HTTP_404_NOT_FOUND: "Not Found",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Internal Server Error",
        },
        operation_description="Retrieve a book by ID",
    )
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a book by ID.
        """
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=BookSerializer,
        responses={
            status.HTTP_200_OK: BookSerializer(),
            status.HTTP_400_BAD_REQUEST: "Bad Request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_403_FORBIDDEN: "Forbidden",
            status.HTTP_404_NOT_FOUND: "Not Found",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Internal Server Error",
        },
        operation_description="Update a book by ID",
    )
    def update(self, request, *args, **kwargs):
        """
        Update a book by ID.
        """
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_204_NO_CONTENT: "No Content",
            status.HTTP_400_BAD_REQUEST: "Bad Request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_403_FORBIDDEN: "Forbidden",
            status.HTTP_404_NOT_FOUND: "Not Found",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Internal Server Error",
        },
        operation_description="Delete a book by ID",
    )
    def destroy(self, request, *args, **kwargs):
        """
        Delete a book by ID.
        """
        return super().destroy(request, *args, **kwargs)

class BookDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows books to be viewed by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    """
    API endpoint that allows books to be created.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListView(generics.ListAPIView):
    """
    API endpoint that lists all books with authors and categories.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @swagger_auto_schema(
        responses={200: BookSerializer(many=True)},
        operation_description="List all books with authors and categories",
    )
    def list(self, request, *args, **kwargs):
        authors = Author.objects.all()
        categories = Category.objects.all()
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        context = {
            'authors': authors,
            'categories': categories,
            'books': serializer.data,
        }
        return render(request, 'bookstore_app/book_list.html', context)

class UserRegistrationView(generics.CreateAPIView):
    """
    API endpoint that allows user registration.
    """
    serializer_class = UserSerializer

    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            status.HTTP_201_CREATED: UserSerializer(),
            status.HTTP_400_BAD_REQUEST: "Bad Request",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Internal Server Error",
        },
        operation_description="Register a new user",
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  
        user = serializer.save()
        return Response({'user_id': user.id, 'username': user.username}, status=status.HTTP_201_CREATED)

class UserLoginView(ObtainAuthToken):
    """
    API endpoint that allows user login.
    """
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            },
            required=['username', 'password'],
        ),
        responses={
            status.HTTP_200_OK: UserSerializer(),
            status.HTTP_400_BAD_REQUEST: "Bad Request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Internal Server Error",
        },
        operation_description="Log in with a user account",
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'token': token.key,
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
