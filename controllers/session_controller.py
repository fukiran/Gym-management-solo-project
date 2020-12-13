from flask import Flask, Blueprint, render_template, request, redirect
from repositories.session_repository import Session
from repositories.booking_repository import Booking
import repositories.session_repository as session_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository
import pdb 

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
@sessions_blueprint.route("/sessions/new", methods=['POST'])
def create_session():
    name = request.form["name"]
    description = request.form["description"]
    upcoming = True
    new_session = Session(name, description, upcoming)
    session_repository.save(new_session)
    return redirect("/sessions")

#edit session form
# @sessions_blueprint.route("/sessions/<id>/edit")
# def edit_session(id):
#     session = session_repository.select(id)
#     return render_template("sessions/edit.html", session=session,)

#update session
@sessions_blueprint.route("/sessions/<id>", methods=['POST','GET'])
def update_session(id):
    if request.method == 'POST':
        name = request.form["name"]
        description = request.form["description"]
        upcoming = request.form["upcoming"]
        session = Session(name, description, upcoming, id)
        session_repository.update(session)

        booked_member_id = request.form["booked_member_id"]
        if booked_member_id != "0":    
            booking = Booking(member_repository.select(booked_member_id),session_repository.select(id))   
            booking_repository.save(booking)
            
        return redirect("/sessions")
    else:
        session = session_repository.select(id)
        booked_members = session_repository.select_booked_members(id)
        all_members = member_repository.select_all()
        return render_template("/sessions/edit.html", id=id, session=session, booked_members=booked_members, all_members=all_members)


