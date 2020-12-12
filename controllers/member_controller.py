from flask import Flask, Blueprint, render_template, request, redirect
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

#show all members
@members_blueprint.route("/members")
def all_members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)


#new member form
@members_blueprint.route("/members/new")
def new_member():
    return render_template("/members/new.html")

#create new member
@members_blueprint.route("/members",methods=['POST'])
def create_member():
    name = request.form["name"]
    age = request.form["age"]
    new_member = Member(name, age)
    member_repository.save(new_member)
    return redirect("/members/index.html")

#edit session form
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("/members/edit.html", member=member)

#update member
@members_blueprint.route("/members/<id>",methods=['POST'])
def update_member(id):
    name = request.form["name"]
    age = request.form["age"]
    member = Member(name, age, id)
    member_repository.update(member)
    return redirect("/members/index.html")