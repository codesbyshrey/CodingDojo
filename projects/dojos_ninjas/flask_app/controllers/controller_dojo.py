from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.model_dojo import Dojo
from datetime import datetime


@app.route("/dojo/create", methods=["POST"])
def dojo_create():
    data = {
        "name": request.form["name"],
    }
    Dojo.create(data)
    return redirect("/dojos")


@app.route("/dojo/edit/<int:id>")
def dojo_edit(id):
    data = {
        "id": id
    }
    session["dojo"] = Dojo.read_one(data)
    return render_template("edit_dojo.html", dojo=session["dojo"])

@app.route("/dojo/edit/submit", methods=["POST"])
def dojo_edit_submit():
    id = request.form["id"]
    data = {
        "id": id,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        "time": datetime.now(),
    }
    Dojo.update_one(data)
    return redirect(f"/dojo/get/{id}")


@app.route("/dojo/delete/<int:id>")
def dojo_delete(id):
    data = {
        "id": id
    }
    Dojo.delete(data)
    return redirect("/dojos")


@app.route("/dojo/<int:id>/get_ninjas")
def dojo_get_ninjas(id):
    data = {
        "id": id
    }
    dojo = Dojo.read_ninjas(data)
    return render_template("read_dojo.html", dojo=dojo)


@app.route("/dojos")
def dojos_show():
    dojos = Dojo.read_all()
    return render_template("read_dojos.html", dojos=dojos)