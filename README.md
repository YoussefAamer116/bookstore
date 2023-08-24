# bookstore
# Bookstore API

This is the Bookstore API, a Django-based web API for managing books, authors, and categories. It provides various endpoints for interacting with the bookstore's data.

## Table of Contents

- [Overview](#overview)
- [Bookstore API Documentation](#bookstore-api-documentation)
- [Setup Instructions](#setup-instructions)
- [Contributing](#contributing)
- [Postman](#Testing_with_Postman)


## Overview

The Bookstore API allows you to perform CRUD (Create, Read, Update, Delete) operations on books, authors, and categories. It also includes user registration and authentication features. You can use this API to build applications like online bookstores, library management systems, and more.

## Bookstore API Documentation

For detailed information on how to use the API, refer to the [API Documentation](#bookstore-api-documentation) section in the [API.md](API.md) file.

## Setup Instructions

### First Method: 
  Follow these instructions to set up and run the Bookstore API locally.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- Django and Django REST framework installed. You can install them using pip:

```bash
pip install django
pip install djangorestframework

```
### Installation
- Clone the repository to your local machine:
```bash
git clone https://github.com/YoussefAamer116/bookstore.git
```
- Navigate to the project directory:
```bash
cd bookstore
```
- Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
```
- Install the project dependencies:
```bash  
pip install -r requirements.txt
```
- Apply the database migrations:
```bash
python manage.py migrate
```
- Start the development server:
```bash
python manage.py runserver
```

### Second Method: 
  Follow these instructions to set up and run the Bookstore API from accessing AWS server(EC2 Instance).

- Download the private key file named bookstore_key.pem.

- Open a command prompt and run the following command to access the AWS EC2 instance:

```bash
ssh -i "path/of/the/file/bookstore_key.pem" ubuntu@13.48.149.66
```
- Once you are connected to the Ubuntu server, navigate to the project directory:

```bash
cd bookstore
```
- Activate the virtual environment:
```bash
source venv_bookstore/bin/activate
```
- Run the server:
```bash
python manage.py runserver 0.0.0.0:8000
  ```
These instructions will help you set up and run the Bookstore API both locally and on an AWS EC2 instance. Make sure to replace "path/of/the/file\bookstore_key.pem" with the actual path to your private key file.

# Bookstore API Documentation

This API documentation provides details about the endpoints, request methods, authentication, and usage of the Bookstore API.

## Authentication

To access certain endpoints, you need to be authenticated. Use the following endpoint to log in and obtain an authentication token:

- **UserLoginView**
  - `POST /login/`: Log in and obtain an authentication token.

### Endpoints

#### Author Endpoints

- **AuthorViewSet**
  - `GET /authors/`: List all authors.
  - `POST /authors/`: Create a new author.
  - `GET /authors/{id}/`: Retrieve an author by ID.
  - `PUT /authors/{id}/`: Update an author by ID.
  - `DELETE /authors/{id}/`: Delete an author by ID.

#### Category Endpoints

- **CategoryViewSet**
  - `GET /categories/`: List all categories.
  - `POST /categories/`: Create a new category.
  - `GET /categories/{id}/`: Retrieve a category by ID.
  - `PUT /categories/{id}/`: Update a category by ID.
  - `DELETE /categories/{id}/`: Delete a category by ID.

#### Book Endpoints

- **BookViewSet**
  - `GET /books/`: List all books with pagination and filtering.
  - `POST /books/`: Create a new book.
  - `GET /books/{id}/`: Retrieve a book by ID.
  - `PUT /books/{id}/`: Update a book by ID.
  - `DELETE /books/{id}/`: Delete a book by ID.

- **BookDetailView**
  - `GET /books/{id}/detail/`: Retrieve a book by ID.

- **BookCreateView**
  - `POST /books/create/`: Create a new book.

- **BookListView**
  - `GET /books/list/`: List all books with authors and categories.

#### User Endpoints

- **UserRegistrationView**
  - `POST /registration/`: Register a new user.

### Pagination and Filtering

- Pagination is applied to the `GET /books/` endpoint with a default page size of 10.
- Filtering is available based on the book's category and author's name.

### Swagger Auto Schema

- The `@swagger_auto_schema` decorator is used to provide detailed descriptions for each endpoint, including request/response formats and operation descriptions.

### Error Handling

- The code handles validation errors and returns appropriate error responses.

To access authenticated endpoints, include the obtained authentication token in your request headers.

## Testing_with_Postman

You can use Postman to interact with the Bookstore API and test its endpoints. Follow these steps to get started:

1. [Download and Install Postman](https://www.postman.com/downloads/): If you don't already have Postman installed on your system, you can download it from the official website.

2. Import the Postman Collection:
   - Download the [Bookstore_test collection](https://api.postman.com/collections/29234170-0e5d0014-7f2c-48dc-b977-681479235fe7?access_key=PMAT-01H8M7RJS3YKC0CB8MTW5CM3CV).
   - Open Postman and click the "Import" button in the top left corner.
   - Select the downloaded collection file (JSON format) and click "Open."

3. Set Up Environment Variables (Optional):
   - You can create environment variables to store the API base URL if you plan to test against different environments (e.g., local, staging, production).
   - Click the gear icon in the top right corner, then click "Add" to create a new environment.
   - Define a variable called `base_url` and set its value to your API's base URL (e.g., `http://localhost:8000`).

4. Start Making Requests:
   - Open the imported collection in Postman.
   - Use the predefined requests to interact with the API endpoints.
   - If you set up environment variables, make sure to select the correct environment for your requests.

5. Run Tests:
   - Some requests in the collection may include tests that verify the API's behavior.
   - Click the "Send" button to execute a request, and check the test results in the response.

6. Explore and Customize:
   - Feel free to explore and customize the requests in the collection to suit your testing needs.
   - You can add new requests or modify existing ones as required.

By using Postman, you can efficiently test and interact with the Bookstore API, making it easier to develop and debug your applications.




## Usage

To use the API, follow the authentication process and make requests to the relevant endpoints based on your requirements. Be sure to check the Swagger or drf-yasg-generated documentation for detailed request/response formats and examples.


## Contributing

If you'd like to contribute to this project, please follow our Contributing Guidelines.
