from flask import Flask, Blueprint, render_template, request, redirect

import repositories.session_repository as session_repository

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/home")
def up_sessions():
    upcoming = session_repository.show_upcoming()
    return render_template("sessions/index.html", upcoming = upcoming)

