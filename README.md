HTTP Mothode:
1-GET:
http://127.0.0.1:5000/books

2-GET book with specific ID:
http://127.0.0.1:5000/books/2 
OR
http://127.0.0.1:5000/books/1
OR 
http://127.0.0.1:5000/books/3

3-POST
http://127.0.0.1:5000/books 
and using jsonfy data like: {
    "title": "New Book",
    "author": "New Author"
}

4-PUT for updated data 
http://127.0.0.1:5000/books/1 
and update data using data like 
{
    "title": "Updated Book Title",
    "author": "Updated Author"
}

5-DELETE
http://127.0.0.1:5000/books/3
