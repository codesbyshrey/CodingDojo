from flask_app import app
from flask import render_template, session, request, redirect
from flask_app.models.dojo_model import Dojo


@app.route("/dojo/create", methods=['POST'])
def dojo_create():
    data = request.form
    Dojo.create(data)
    return redirect("/")

@app.route("/dojo/<int:id>")
def dojo_show(id):
    data = {'id' : id}
    dojo = Dojo.get_one_with_many(data)
    print(dojo.ninjas)
    return render_template("dojo_show.html", dojo=dojo)