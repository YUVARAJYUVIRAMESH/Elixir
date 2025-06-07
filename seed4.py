from main import returnDb, createApp  # Update with your actual app context
from models import Books  # Update with your model file path

app = createApp()
db = returnDb()

with app.app_context():  # 👈 This ensures db.session works
    books_to_add = [
        Books(
            name="Atomic Habits",
            isbn="9780735211292",
            author="James Clear",
            category="Self-help",
            image_url="https://images-na.ssl-images-amazon.com/images/I/91bYsX41DVL.jpg",
            description="A practical guide to building good habits and breaking bad ones."
        ),
        Books(
            name="The Power of Now",
            isbn="9781577314806",
            author="Eckhart Tolle",
            category="Self-help",
            image_url="https://images-na.ssl-images-amazon.com/images/I/81IuG6wU2iL.jpg",
            description="A spiritual guide to help you live fully in the present moment."
        ),
        Books(
            name="The 7 Habits of Highly Effective People",
            isbn="9780743269513",
            author="Stephen R. Covey",
            category="Self-help",
            image_url="https://images-na.ssl-images-amazon.com/images/I/71uwocAMtaL.jpg",
            description="Timeless principles for personal and professional effectiveness."
        ),
        Books(
            name="Can't Hurt Me",
            isbn="9781544512280",
            author="David Goggins",
            category="Self-help",
            image_url="https://images-na.ssl-images-amazon.com/images/I/81ww3bZ4hZL.jpg",
            description="A memoir of resilience and mental toughness."
        ),

Books(
    name="The Immortal Life of Henrietta Lacks",
    isbn="9781400052189",
    author="Rebecca Skloot",
    category="Non-Fiction",
    image_url="https://m.media-amazon.com/images/I/81WcnNQ-TBL._SL1500_.jpg",
    description="Chronicles the life of Henrietta Lacks and her immortal cell line, HeLa."
),

Books(
    name="Born a Crime",
    isbn="9780399588198",
    author="Trevor Noah",
    category="Non-Fiction",
    image_url="https://m.media-amazon.com/images/I/81aY1lxk+PL._SL1500_.jpg",
    description="A humorous memoir detailing Noah’s experiences growing up in apartheid South Africa."
),
        Books(
    name="Educated",
    isbn="9780399590504",
    author="Tara Westover",
    category="Non-Fiction",
    image_url="https://m.media-amazon.com/images/I/81WojUxbbFL._SL1500_.jpg",
    description="A memoir about a woman who grows up in a strict and abusive household in rural Idaho but eventually escapes to learn about the wider world through education."
),
        Books(
    name="Sapiens: A Brief History of Humankind",
    isbn="9780062316097",
    author="Yuval Noah Harari",
    category="Non-Fiction",
    image_url="https://m.media-amazon.com/images/I/713jIoMO3UL._SL1500_.jpg",
    description="Explores the history of humankind from the Stone Age to the modern age."
),
        Books(
    name="A Brief History of Time",
    isbn="9780553109535",
    author="Stephen Hawking",
    category="Science",
    image_url="https://m.media-amazon.com/images/I/71SxZ8d3R-L._SL1500_.jpg",
    description="An exploration of fundamental questions about the universe, including the nature of time, black holes, and the Big Bang."
),
        Books(
    name="Cosmos",
    isbn="9780345539434",
    author="Carl Sagan",
    category="Science",
    image_url="https://m.media-amazon.com/images/I/71tbalAHYCL._SL1500_.jpg",
    description="A journey through space and time, exploring the universe and our place within it."
),
        Books(
    name="The Selfish Gene",
    isbn="9780198788607",
    author="Richard Dawkins",
    category="Science",
    image_url="https://m.media-amazon.com/images/I/81t2CVWEsUL._SL1500_.jpg",
    description="Introduces the gene-centered view of evolution and the concept of memes as units of cultural transmission."
),
        Books(
    name="A Short History of Nearly Everything",
    isbn="9780767908184",
    author="Bill Bryson",
    category="Science",
    image_url="https://m.media-amazon.com/images/I/81WcnNQ-TBL._SL1500_.jpg",
    description="A comprehensive overview of scientific discoveries, from the Big Bang to the rise of civilization."
)



    ]
    
    db.session.add_all(books_to_add)
    db.session.commit()
