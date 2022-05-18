from flask import Blueprint, request
from project.controllers.player.player_controller import PlayerController
from project.models.player import Player
from project.utils.encoder import Object

players = Blueprint("players", __name__)

@players.route("/player", methods=["POST"])
def create():
    try:    
        body = request.get_json()
        player:Player = {
            "name":body["name"],
            "goals":body["goals"],
            "id":body["id"]
            }
        player = PlayerController(player,body["fk"])
        player.save()
        return f"El Jugador con id: {id} a sido creado", 200
    except Exception as e:
        return {"error":str(e)}, 400

@players.route("/players", methods=["GET"])
def get_all():
    try:    
        playerController = PlayerController()
        players = playerController.get_all()
        return {"players":players}
    except Exception as e:
        return {"error":str(e)}, 400

@players.route("/player/<id>", methods=["DELETE"])
def delete(id):
    try:
        playerController = PlayerController()
        playerController.delete(id)
        return f"El Jugador con id: {id} a sido eliminado", 200
    except Exception as e:
        return {"error":str(e)}, 400

@players.route("/player/<id>", methods=["GET"])
def get_by_id(id):
    try:
        playerController = PlayerController()
        player = playerController.get_by_id(id)
        return {"player":player}
    except Exception as e:
        return {"error":str(e)}, 400

@players.route("/player/<id>", methods=["PUT"])
def update(id):
    try:
        body = request.get_json()
        player:Player = {
            "name":body["name"],
            "goals":body["goals"],
            "id":body["id"],
            }
        player = PlayerController(player,0)
        response = player.update(id)
        return f"El Jugador con id: {id} a sido actualizado", 200
    except Exception as e:
        return {"error":str(e)}, 400