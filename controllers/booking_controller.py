from flask import Flask, Blueprint, render_template, request, redirect


bookings_blueprint = Blueprint("bookings", __name__)

#admin route
@bookings_blueprint.route('/admin')
def admin_panel():
    return render_template("/admin/index.html")