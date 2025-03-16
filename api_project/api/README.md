# API Authentication & Permissions Setup

## 1. Authentication

### a) Obtaining a Token
To authenticate, send a **POST** request to:

http://127.0.0.1:8000/api/api-token-auth/

with the following JSON body:
```json
{
    "username": "admin-help",
    "password": "Qwertykey1!@"
}


This will return an authentication token.

Quick Method to Get a Token
Instead of making a manual request, you can run the generate_token.py script (you need to be in the project folder):

python generate_token.py

It will prompt for a username and generate a token automatically.


b) Using the Token
For all requests requiring authentication, include the token in the Authorization header:

Authorization: Token your_token_here


2. Permissions
a) Current Permission Settings
The BooksViewSet is configured with:

permission_classes = [permissions.IsAuthenticatedOrReadOnly]

This means:

✅ Anyone (even unauthenticated users) can view books.
🔒 Only authenticated users can create, update, or delete books.
b) Changing Permissions
To make the API fully restricted so that only logged-in users can even read books, update views.py:

permission_classes = [permissions.IsAuthenticated]  # Now only logged-in users can access any part of the API


3. API Endpoints & Testing Requests
a) Get All Books (Public Access)
Anyone can call this endpoint (authentication is not required).

curl -X GET http://127.0.0.1:8000/api/books_all/    # if you use windows and curl doesnt work access with postman 

b) Create a Book (Requires Authentication)
Only authenticated users can create a book.

curl -X POST http://127.0.0.1:8000/api/books_all/ \
-H "Authorization: Token your_token_here" \
-H "Content-Type: application/json" \
-d '{"title": "New Book", "author": "Authenticated User"}'

c) Retrieve a Single Book by ID (Public Access)
curl -X GET http://127.0.0.1:8000/api/books_all/1/


d) Update a Book (Requires Authentication)
curl -X PUT http://127.0.0.1:8000/api/books_all/1/ \
-H "Authorization: Token your_token_here" \
-H "Content-Type: application/json" \
-d '{"title": "Updated Title", "author": "Updated Author"}'


e) Delete a Book (Requires Authentication)
curl -X DELETE http://127.0.0.1:8000/api/books_all/1/ \
-H "Authorization: Token your_token_here"


4. Main API Endpoint
All book-related API operations are available at:
http://127.0.0.1:8000/api/books_all/


Example: Retrieve a book with ID 1:
http://127.0.0.1:8000/api/books_all/1/


5. Additional Notes
The API follows RESTful principles, meaning it supports CRUD operations (Create, Read, Update, Delete).
The authentication method used is Token Authentication via rest_framework.authtoken.
Permissions are configured using DRF’s permission classes.