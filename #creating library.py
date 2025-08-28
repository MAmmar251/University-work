library = {
    "978-3-16-148410-0": 
        {"title": "Python Programming",
        "author": "John Doe",
        "publication_year": 2020},
    "978-1-60309-452-8": 
        {"title": "Data Science Essentials",
        "author": "Jane Smith",
        "publication_year": 2021}
    ,
    "978-0-12345-678-9": 
        {"title": "Machine Learning Basics",
        "author": "Alice Johnson",
        "publication_year": 2022}
}

def check_book(isbn):
  if isbn in library:
    book = library[isbn]
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Publication Year: {book['publication_year']}")
  else:
    print("Book not found.")
user_isbn = input("Enter the ISBN of the book:")
check_book(user_isbn)