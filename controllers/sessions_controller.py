from flask import Flask, Blueprint, render_template, request, redirect, flash
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
    capacity = request.form["capacity"]
    upcoming = True
    offpeak = request.form["offpeak"]
    new_session = Session(name, description, upcoming, capacity, offpeak)
    session_repository.save(new_session)
    return redirect("/sessions")


#update session
@sessions_blueprint.route("/sessions/<id>", methods=['POST','GET'])
def update_session(id):
    if request.method == 'POST':
        name = request.form["name"]
        description = request.form["description"]
        upcoming = request.form["upcoming"]
        capacity = request.form["capacity"]
        offpeak = request.form["offpeak"]
        session = Session(name, description, upcoming, capacity, offpeak, id)
        session_repository.update(session)

        if int(capacity) > session_repository.how_many_members(id):

            booked_member_id = request.form["booked_member_id"]
            if booked_member_id != "0":  
                booking = Booking(member_repository.select(booked_member_id),session_repository.select(id))   
                booking_repository.save(booking)

            return redirect("/sessions")
        
        return redirect("/sessions")

    else:
        session = session_repository.select(id)
        booked_members = session_repository.select_booked_members(id)
        if session.offpeak == False:
            members = member_repository.select_all_premium_active_members()
        else:
            members = member_repository.select_active()

        capacity = session_repository.select(id)
        spaces_taken = session_repository.how_many_members(id)

        if int(capacity.capacity) <= spaces_taken:
            flash(' This class is full, no more bookings available!!!')
        return render_template("/sessions/edit.html", id=id, session=session, booked_members=booked_members, members=members)


