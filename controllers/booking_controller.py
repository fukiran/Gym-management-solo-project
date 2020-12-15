from flask import Flask, Blueprint, render_template, request, redirect
import repositories.session_repository as session_repository

bookings_blueprint = Blueprint("bookings", __name__)

#admin route
@bookings_blueprint.route('/admin')
def admin_panel():
    past_sessions = session_repository.show_past_sessions()
    return render_template("/admin/index.html", past_sessions=past_sessions)