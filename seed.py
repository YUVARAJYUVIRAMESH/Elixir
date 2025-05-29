from main import createApp
from models import db, Books
import os

app = createApp()
# Default image for all books (you can change this to real image names if available)
DEFAULT_IMAGE = "static/image/default.jpg"

# Sample books to insert
books_data = [
    {
        "name": "The Alchemist",
        "isbn": "9780061122415",
        "genre": "Fiction",
        "image_url": DEFAULT_IMAGE,
        "description": "A shepherd's journey to discover his personal legend."
    },
    {
        "name": "Atomic Habits",
        "isbn": "9780735211292",
        "genre": "Self-help",
        "image_url": DEFAULT_IMAGE,
        "description": "Strategies for building good habits and breaking bad ones."
    },
    {
        "name": "1984",
        "isbn": "9780451524935",
        "genre": "Dystopian",
        "image_url": DEFAULT_IMAGE,
        "description": "A chilling depiction of perpetual war and government surveillance."
    },
    {
        "name": "Harry Potter and the Sorcerer's Stone",
        "isbn": "9780590353427",
        "genre": "Fantasy",
        "image_url": DEFAULT_IMAGE,
        "description": "The magical journey begins for Harry Potter."
    },
    {
        "name": "To Kill a Mockingbird",
        "isbn": "9780061120084",
        "genre": "Classic",
        "image_url": DEFAULT_IMAGE,
        "description": "A tale of racial injustice in the American South."
    },
]

# Add 25 more sample books
for i in range(6, 31):
    books_data.append({
        "name": f"Sample Book {i}",
        "isbn": f"97800000000{i}",
        "genre": "Fiction",
        "image_url": DEFAULT_IMAGE,
        "description": f"Description of sample book {i}."
    })

# Insert into database
with app.app_context():
    # Optional: clear existing books (uncomment if needed)
    # db.session.query(Books).delete()

    for book in books_data:
        new_book = Books(**book)
        db.session.add(new_book)

    db.session.commit()
    print("✅ 30 books added successfully.")
