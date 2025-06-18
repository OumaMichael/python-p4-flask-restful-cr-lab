from app import app
from models import db, Plant

class TestPlant:
    def test_plants_get_route_returns_list_of_plant_objects(self):
        with app.app_context():
            p = Plant(name="Douglas Fir", image="http://example.com/image.png", price=19.99)
            db.session.add(p)
            db.session.commit()

            client = app.test_client()
            response = client.get("/plants")
            assert response.status_code == 200
            data = response.get_json()
            assert isinstance(data, list)
            assert any(plant["name"] == "Douglas Fir" for plant in data)
