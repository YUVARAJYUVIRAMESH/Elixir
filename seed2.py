from main import returnDb, createApp  # Update with your actual app context
from models import Books  # Update with your model file path
import random
from faker import Faker

app = createApp()
db = returnDb()

fake = Faker()
# Base path for images
with app.app_context():  # 👈 This ensures db.session works
    image_base = '/static/image/'
    image_urls = ["photo-1.jpg", "photo-2.jpg", "photo-3.jpg", "photo-4.png", "photo-5.jpeg", "photo-6.jpeg", "photo-7.avif", "photo-8.avif", "photo-9.avif", "photo-10.avif", "photo-11.avif", "photo-12.avif", "photo-13.avif", "photo-14.avif", "photo-15.avif", "photo-16.avif", "photo-17.avif", "photo-18.avif", "photo-19.avif", "photo-20.avif", "photo-21.avif", "photo-22.avif", "photo-23.avif", "photo-24.avif", "photo-25.avif"]


    Category = ["Fiction", "Non-Fiction", "Education", "Philosophy", "Art",
                "Biography", "Self-Help", "Science", "History", "Buisness", "Humour"]
    # Create and insert 20 fiction books
    for j in range(0, 9):
        for i in range(1, 41):
            book = Books(
                name=fake.sentence(nb_words=3).replace('.', ''),
                isbn=fake.isbn13(),
                category=random.choice(Category),
                author = fake.name(),
                # e.g., /static/image/fiction1.jpg
                image_url= f"{image_base}{random.choice(image_urls)}",               description=fake.text(max_nb_chars=180)
            )
            db.session.add(book)

    db.session.commit()
    print("✅ 20 fiction books added.")
