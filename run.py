from main import createApp
from main import returnDb


app = createApp()
db = returnDb()

if __name__ == "__main__":

    with app.app_context():
        db.create_all()
        app.run(debug=True)
