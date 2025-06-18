#!/usr/bin/env python3

from app import app
from models import db, Plant

if __name__ == '__main__':
    with app.app_context():
        # Optional: seed if needed
        # db.session.add(Plant(name="Test Plant", image="test.jpg", price=9.99))
        # db.session.commit()

        # Start debugging session
        import ipdb; ipdb.set_trace()

