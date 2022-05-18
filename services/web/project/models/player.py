
from sqlalchemy import ForeignKey
from project.database.manager import db

class Player(db.Model):

    __tablename__ = "players"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    goals = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    fk_team = db.Column(db.Integer, ForeignKey('team.id'), nullable=False)
    activate = db.Column(db.Boolean(), default=True, nullable=False)
