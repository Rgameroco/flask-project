from datetime import datetime
from project.models.team import Team
from project.models.player import Player
from datetime import datetime
from project.database.manager import db
from sqlalchemy.sql import func

class TeamController:
    def __init__(self, team= None):
        if team == None:
            self.id = None
            self.name = None
            self.city = None
            self.time = datetime.now()
        else:    
            self.id = team["id"]
            self.name = team["name"]
            self.city = team["city"]
            self.time = datetime.now()

    def save(self):
        team = Team(
            id=self.id,
            name=self.name,
            city=self.city,
            created_at=self.time,
            updated_at=self.time
        )
        db.session.add(team)
        db.session.commit()
        return team
    
    def update(self,id):
        team = Team.query.filter_by(
            id=id,
            activate=True
            ).first()
        team.name = self.name
        team.city = self.city
        team.time = self.time
        team.updated_at = self.time
        db.session.add(team)
        db.session.commit()
        return team
    
    def delete(self,id):
        team = Team.query.filter_by(id=id).first()
        team.activate = False
        db.session.add(team)
        db.session.commit()
        return team
    
    def get_all(self):
        teams = Team.query.filter_by(activate=True).all()
        return self.deserialize(teams)

    def get_by_id(self,id):
        team = Team.query.filter_by(id=id,activate=True).all()
        return self.deserialize(team)

    def deserialize(self, teams):
        print("deserialize")
        listTeams = []
        for team in teams:
            dictiPlayers = {}
            dictiPlayers["id"] = team.id
            dictiPlayers["name"] = team.name
            dictiPlayers["city"] = team.city
            dictiPlayers["created_at"] = team.created_at
            dictiPlayers["updated_at"] = team.updated_at
            dictiPlayers["goals_count"] = self.sumGoals(team.id)
            listTeams.append(dictiPlayers)
        return listTeams

    def sumGoals(self,id):
        query = Player.query.with_entities(func.sum(Player.goals)).filter_by(fk_team=id,activate=True).all()
        return query[0][0]