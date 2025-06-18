from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Plant

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/plants")
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.to_dict() for plant in plants])

@app.route("/plants/<int:id>")
def get_plant(id):
    plant = Plant.query.get(id)
    if plant:
        return jsonify(plant.to_dict())
    return jsonify({"error": "Plant not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
