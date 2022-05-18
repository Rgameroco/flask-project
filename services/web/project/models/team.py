from project.database.manager import db

class Team(db.Model):

    __tablename__ = "team"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    city = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    activate = db.Column(db.Boolean(), default=True, nullable=False)