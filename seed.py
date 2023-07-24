# seed.py
from models import db, connect_db, Cupcake
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


def seed_data():
    """Seed database with some example data."""

    # Add sample cupcakes
    cupcake1 = Cupcake(
        flavor="Chocolate",
        size="Large",
        rating=9.0,
        image="https://example.com/image1.jpg"
    )

    cupcake2 = Cupcake(
        flavor="Vanilla",
        size="Small",
        rating=8.0,
        image="https://example.com/image2.jpg"
    )

    db.session.add(cupcake1)
    db.session.add(cupcake2)

    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_data()
