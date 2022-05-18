from flask import Blueprint, request
from project.controllers.team.team_controller import TeamController
from project.models.team import Team

team = Blueprint("team", __name__)

@team.route("/team", methods=["POST"])
def create():
    try:
        body = request.get_json()
        team:Team = {
            "id":body["id"],
            "name":body["name"],
            "city":body["city"],
            }
        team = TeamController(team)
        team.save()
        return f"El Equipo con id: {id} a sido actualizado", 200
    except Exception as e:
        return {"error":str(e)}, 400

@team.route("/teams", methods=["GET"])
def get_all():
    try:
        teamController = TeamController()
        teams = teamController.get_all()
        return {"teams":teams}, 200
    except Exception as e:
        return {"error":str(e)}, 400

@team.route("/team/<id>", methods=["DELETE"])
def delete(id):
    try:
        teamController = TeamController()
        teamController.delete(id)
        return f"El Equipo con id: {id} a sido actualizado", 200
    except Exception as e:
        return {"error":str(e)}, 400

@team.route("/team/<id>", methods=["GET"])
def get_by_id(id):
    try:
        teamController = TeamController()
        team = teamController.get_by_id(id)
        return {"team":team}, 200
    except Exception as e:
        return {"error":str(e)}, 400

@team.route("/team/<id>", methods=["PUT"])
def update(id):
    try:
        body = request.get_json()
        team:Team = {
            "id":body["id"],
            "name":body["name"],
            "city":body["city"],
            }
        team = TeamController(team)
        response = team.update(id)
        return f"El Equipo con id: {id} a sido actualizado", 200
    except Exception as e:
        return {"error":str(e)}, 400