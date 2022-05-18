import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project.routes.player import players
from project.routes.team import team

app = Flask(__name__)
app.config.from_object("project.config.Config")
app.register_blueprint(players)
app.register_blueprint(team)
print(app.config)
SQLAlchemy(app)



