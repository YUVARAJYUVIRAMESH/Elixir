from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from functions import imagePathCoder
from models import Books, Users, BooksRented, db
from sqlalchemy import or_
from flask_login import login_user, login_required, logout_user, current_user
import os



def callRoutes(app, login_manager):

    routes = Blueprint("routes", __name__, template_folder = "templates")



    login_manager.login_view = "routes.login"


    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))


    @routes.route('/')
    def home():

        print(url_for('routes.admin'))
        return render_template("home.html")


    @routes.route("/adminn")
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


    @routes.route("/insert", methods=["POST"])
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

        return redirect(url_for('routes.admin', db=dab))


    @routes.route("/edit", methods = ["POST"])
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
        return redirect(url_for("routes.admin", db=dab))


    @routes.route("/delete")
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

        return redirect(url_for("routes.admin", db = dab))


    @routes.route("/login", methods = ["GET", "POST"])
    def login():
        if request.method == "POST":
            name = request.form.get("name")
            password = request.form.get("password")

            user = Users.query.filter(or_(Users.username == name, Users.email == name)).first()
            print(user)

            if user:
                if (user.password == password):
                    login_user(user)
                    return redirect(url_for("routes.home"))

            else:
                flash("Invalid User Credentials")

        return render_template("login.html")

    @routes.route("/register", methods = ["GET", "POST"])
    def register():

        if (request.method == "POST"):
            name = request.form.get("name")
            email = request.form.get("email")
            password = request.form.get("password")

            user = Users(name, email, password)
            db.session.add(user)
            db.session.commit()
            
        return render_template("register.html")




    @routes.route("/logout")
    @login_required
    def logout():
        logout_user()

        return redirect(url_for("routes.login"))

    @routes.route("/api/searchBooks")
    def api_SearchBooks():
        query = request.args.get("q", "")
        if not query:
            return jsonify([])

        books = Books.query.filter(Books.name.ilike(f"%{query}%")).all()
        return jsonify([{"id": book.id, "name": book.name} for book in books])

    @routes.route("/profile")
    @login_required
    def profile():
        return render_template("profile.html", user = current_user)

    return routes



