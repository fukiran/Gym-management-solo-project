from flask import Flask, Blueprint, render_template, request, redirect
from repositories.session_repository import Session
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint("sessions", __name__)

#show upcoming sessions
@sessions_blueprint.route("/sessions")
def up_sessions():
    upcoming = session_repository.show_upcoming()
    return render_template("sessions/index.html", upcoming = upcoming)

#new session form
@sessions_blueprint.route("/sessions/new", methods=['GET'])
def new_session():
    return render_template("sessions/new.html")

#create new session
@sessions_blueprint.route("/sessions", methods=['POST'])
def create_session():
    name = request.form["name"]
    description = request.form["description"]
    upcoming = True
    new_session = Session(name, description, upcoming)
    session_repository.save(new_session)
    return redirect("/sessions")

#edit session form
@sessions_blueprint.route("/sessions/<id>/edit")
def edit_session(id):
    session = session_repository.select(id)
    return render_template("sessions/edit.html", session=session)

#update session
@sessions_blueprint.route("/sessions/<id>", methods=['POST'])
def update_session(id):
    name = request.form["name"]
    description = request.form["description"]
    upcoming = request.form["upcoming"]
    session = Session(name, description, upcoming, id)
    session_repository.update(session)
    return redirect("/sessions")


