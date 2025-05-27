from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os


from functions import imagePathCoder

app = Flask(__name__)

app.secret_key = 'vanakam'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(70), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Books(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    isbn = db.Column(db.String(70), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(90), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, name, isbn, genre, image_url, description):

        self.name = name
        self.isbn = isbn
        self.genre = genre
        self.image_url = image_url
        self.description = description


class BooksRented(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    book = db.relationship('Books')
    user = db.relationship('Users')

    def __init__(self, book_id, user_id, created_at=None):

        self.book_id = book_id
        self.user_id = user_id
        self.created_at = created_at or datetime.utcnow()


@app.route('/')
def home():

    print(url_for('admin'))
    return render_template("home.html")


@app.route("/adminn")
def admin():
    dab = request.args.get("db")
    if dab:
        if (dab == "Books"):
            data = Books.query.all()
        elif (dab == "Users"):
            data = Users.query.all()
        elif (dab == "BooksRented"):
            data = BooksRented.query.all()

        return render_template(f"admin{dab}.html", data=data, db=dab)

    return render_template("admin.html")


@app.route("/insert", methods=["POST"])
def insert():
    dab = request.args.get("dab")
    print(dab)

    if (dab == "Books"):

        name = request.form["name"]
        isbn = request.form["isbn"]
        genre = request.form["genre"]
        image = request.files["image"]
        description = request.form["description"]

        image_path = imagePathCoder(image)

        image.save(image_path)
        new_book = Books(name, isbn, genre, image_path, description)
        db.session.add(new_book)
        db.session.commit()


    elif (dab == "Users"):
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        new_user = Users(name, email, password)

        db.session.add(new_user)
        db.session.commit()

    return redirect(url_for('admin', db=dab))


@app.route("/edit", methods = ["POST"])
def edit():
    id = request.args.get("id")
    dab = request.args.get("dab")

    image = request.files.get("image")

    if (image):
        image_Path = imagePathCoder(image)
        image.save(image_Path)

    if (dab == "Books"):
        edit_book = Books.query.get(id)

        edit_book.name = request.form["name"]
        edit_book.isbn = request.form["isbn"]
        edit_book.genre = request.form["genre"]
        edit_book.description = request.form["description"]

        if (image and os.path.exists(edit_book.image_url)):
            os.remove(edit_book.image_url)
            edit_book.image_url = image_Path

        db.session.add(edit_book)
        db.session.commit()


    elif (dab == "Users"):
        edit_user = Users.query.get(id)

        edit_user.username = request.form.get("name")
        edit_user.email = request.form.get("email")
        edit_user.password = request.form.get("password")

        db.session.add(edit_user)
        db.session.commit()

    flash("User edited successfully")
    return redirect(url_for("admin", db=dab))


@app.route("/delete")
def delete():
    dab = request.args.get("db")
    id = request.args.get("id")

    if (dab == "Books"):
        delete_book = Books.query.get(id)
        db.session.delete(delete_book)
        db.session.commit()

    elif (dab == "Users"):
        delete_user = Users.query.get(id)
        db.session.delete(delete_user)
        db.session.commit()

    return redirect(url_for("admin", db = dab))



if __name__ == "__main__":

    with app.app_context():
    

        app.run(debug=True)


