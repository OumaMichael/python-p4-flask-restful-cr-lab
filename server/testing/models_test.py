from app import app
from models import db, Plant

class TestPlant:
    def test_can_be_created(self):
        with app.app_context():
            p = Plant(name="Douglas Fir", image="http://example.com/image.png", price=19.99)
            db.session.add(p)
            db.session.commit()
            assert p.id is not None

    def test_can_be_serialized(self):
        with app.app_context():
            p = Plant(name="Douglas Fir", image="http://example.com/image.png", price=19.99)
            db.session.add(p)
            db.session.commit()
            data = p.to_dict()
            assert data["name"] == "Douglas Fir"
            assert data["image"] == "http://example.com/image.png"
            assert data["price"] == 19.99
