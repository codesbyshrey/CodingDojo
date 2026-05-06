from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo
from datetime import datetime


@app.route("/ninja/create")
def ninja_create():
    return render_template("create_ninja.html")

@app.route("/ninja/create", methods=["POST"])
def ninja_create_submit():
    dojo = request.form["dojo"]
    data = {
        "dojo": dojo,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
    }
    Ninja.create(data)
    return redirect(f"/dojo/{dojo}/get_ninjas")


@app.route("/ninja/edit/<int:id>")
def ninja_edit(id):
    data = {
        "id": id
    }
    session["ninja"] = Ninja.read_one(data)
    return render_template("edit_ninja.html", ninja=session["ninja"])

@app.route("/ninja/edit/submit", methods=["POST"])
def ninja_edit_submit():
    id = request.form["id"]
    data = {
        "id": id,
        "dojoid": request.form["dojoid"],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
        "time": datetime.now(),
    }
    Ninja.update_one(data)
    return redirect(f"/ninja/get/{id}")

@app.route("/ninjas")
def ninjas_show():
    dojos = Dojo.read_all()
    return render_template("create_ninja.html", dojos=dojos)