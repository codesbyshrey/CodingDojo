from flask_app import app
from flask import redirect, request, session, render_template, flash
from flask_bcrypt import Bcrypt
from flask_app.models.model_user import User

bcrypt = Bcrypt(app)

@app.route("/register", methods=["POST"])
def register():
    if not User.validate_create(request.form):
        return redirect("/")
    data = {
        **request.form,
        "password": bcrypt.generate_password_hash(request.form["password"])
    }
    created_user = User.create(data)
    session["user_id"] = created_user
    return redirect("/success")

@app.route("/login", methods=["POST"])
def login():
    if not User.validate_login(request.form):
        return redirect("/")

    data = { "email" : request.form["email"] }
    user_in_db = User.read_one(data)

    if not user_in_db:
        flash("Invalid login credentials.")
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid login credentials.")
        return redirect("/")

    session["user_id"] = user_in_db.id
    return redirect("/success")

@app.route("/logout")
def logout():
    if not "user_id" in session:
        return redirect("/")
    session.pop("user_id")
    return redirect("/")

@app.route("/success")
def success():
    if "user_id" not in session:
        return redirect("/")
    return render_template("success.html", id=session["user_id"])