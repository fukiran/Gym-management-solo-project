from flask import Flask, Blueprint, render_template, request, redirect
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

#show all members
@members_blueprint.route("/members")
def all_members():
    members = member_repository.select_active()
    return render_template("members/index.html", members=members)

#new member form
@members_blueprint.route("/members/new", methods=['GET'])
def new_session():
    return render_template("members/new.html")

#create new member
@members_blueprint.route("/members/new", methods=['POST'])
def new_member():
        name = request.form["name"]
        age = request.form["age"]
        premium = request.form["premium"]
        active = True
        new_member = Member(name, age, premium, active)
        member_repository.save(new_member)
        return redirect("/members")

#edit session form
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("/members/edit.html", member=member)

#update member
@members_blueprint.route("/members/<id>",methods=['POST','GET'])
def update_member(id):
    if request.method == 'POST':
        name = request.form["name"]
        age = request.form["age"]
        premium = request.form["premium"]
        active = request.form['active']
        member = Member(name, age, premium, active, id)
        member_repository.update(member)
        return redirect("/members")
    else:
        member = member_repository.select(id)
        booked_sessions = member_repository.select_classes_booked_for(id)
        return render_template("/members/edit.html",id=id, member=member, booked_sessions=booked_sessions)