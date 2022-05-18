from flask.cli import FlaskGroup
from project import app
from project.database.manager import db
import os

cli = FlaskGroup(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    cli()
