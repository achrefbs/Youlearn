#!/usr/bin/python3
import os
from app import app, db

if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True)