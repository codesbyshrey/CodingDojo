from flask_app import app
from flask import render_template, session, request, redirect
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo



@app.route("/ninja/new")
def ninja_new():
    all_dojos = Dojo.get_all()
    return render_template("new_ninja.html", all_dojos=all_dojos)

@app.route("/ninja/create", methods=['POST'])
def ninja_create():
    data = request.form
    Ninja.create(data)
    return redirect("/")