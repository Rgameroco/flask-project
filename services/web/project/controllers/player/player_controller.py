from time import time

from project.models.player import Player
from datetime import datetime
from project.database.manager import db
from sqlalchemy.sql import func

class PlayerController():

    def __init__(self, player = None, fk_team=None):
        if player == None:
            self.id = None
            self.name = None
            self.goals = None
            self.time = datetime.now()
        else:
            self.id = int(player["id"])
            self.name = player["name"]
            self.goals = int(player["goals"])
            self.time = datetime.now() 
            self.fk_team = int(fk_team)
            

    def save(self):
        print("entrando save")
        player = Player(
            id=self.id,
            name=self.name,
            goals=self.goals,
            created_at=self.time,
            updated_at=self.time,
            fk_team=self.fk_team
        )
        db.session.add(player)
        db.session.commit()
        print("commit")
        return player

    def update(self,id):
        player = Player.query.filter_by(
            id=id,
            activate=True
            ).first()
        player.name = self.name
        player.goals = self.goals
        player.time = self.time
        player.fk_team = self.fk_team
        player.updated_at = self.time
        db.session.add(player)
        db.session.commit()
        return player

    def delete(self,id):
        player = Player.query.filter_by(id=id).first()
        player.activate = False
        db.session.add(player)
        db.session.commit()
        return player

    def get_all(self):
        players = Player.query.filter_by(activate=True).all()
        return self.deserialize(players)
    
    def get_by_id(self,id):
        player = Player.query.filter_by(activate=True,id=id).all()
        return self.deserialize(player)

    def deserialize(self,players):
        listPlayers = []
        for i in players:
            dictiPlayers = {}
            dictiPlayers["id"] = i.id
            dictiPlayers["name"] = i.name
            dictiPlayers["goals"] = i.goals
            dictiPlayers["fk_team"] = i.fk_team
            dictiPlayers["updated_at"] = i.updated_at
            dictiPlayers["created_at"] = i.created_at
            listPlayers.append(dictiPlayers)
        return listPlayers
