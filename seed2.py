from main import returnDb, createApp  # Update with your actual app context
from models import Books  # Update with your model file path
import random
from faker import Faker

app = createApp()
db = returnDb()

fake = Faker()
# Base path for images
with app.app_context():  # 👈 This ensures db.session works
    image_base = '/static/image/fiction'

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
                image_url=f'{image_base}{i}.jpg',
                description=fake.text(max_nb_chars=180)
            )
            db.session.add(book)

    db.session.commit()
    print("✅ 20 fiction books added.")
