from flask_app import app
from flask import render_template, session, request, redirect
from flask_app.models.dojo_model import Dojo


@app.route("/")
def index():
    return redirect("/dojo")

@app.route("/dojo")
def show_dojos():
    all_dojos = Dojo.get_all()
    return render_template("index.html", all_dojos=all_dojos)