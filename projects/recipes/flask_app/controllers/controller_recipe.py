from flask_app import app
from flask import redirect, request, session, render_template
from flask_bcrypt import Bcrypt
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe
import datetime

bcrypt = Bcrypt(app)

@app.route("/recipe/create")
def recipe_create():
    if "user" not in session:
        return redirect("/")
    user_id = session["user"]["id"]
    return render_template("create_recipe.html", user_id=user_id)

@app.route("/recipe/create/submit", methods=["POST"])
def recipe_create_submit():
    if not Recipe.validate(request.form):
        return redirect("/recipe/create")
    Recipe.create(request.form)
    return redirect("/recipes")

@app.route("/recipe/view/<int:id>")
def recipe_view_one(id):
    if "user" not in session:
        return redirect("/")
    recipe = Recipe.read_one_with_user({"id": id})
    return render_template("recipe.html", user=session["user"], recipe=recipe)

@app.route("/recipe/edit/<int:id>")
def recipe_edit(id):
    if "user" not in session:
        return redirect("/")
    recipe = Recipe.read_one_with_user({"id": id})
    date_created = recipe.created_at.strftime('%Y-%m-%d')
    recipe_formatted = {
        **recipe.__dict__,
        "created_at": date_created
    }
    return render_template("edit_recipe.html", user=session["user"], recipe=recipe_formatted)

@app.route("/recipe/edit/<int:id>/submit", methods=["POST"])
def recipe_edit_submit(id):
    if "user" not in session:
        return redirect("/")
    if not Recipe.validate(request.form):
        return redirect(f"/recipe/edit/{id}")
    data = {**request.form, "recipe_id":request.form["recipe_id"]}
    Recipe.update(request.form)
    return redirect(f"/recipe/view/{id}")

@app.route("/recipes")
def recipe_view_all():
    if "user" not in session:
        return redirect("/")
    recipes = Recipe.read_all_with_users()
    return render_template("recipes.html", user=session["user"], recipes=recipes)

@app.route("/recipe/delete/<int:id>")
def delete_one(id):
    if "user" not in session:
        return redirect("/")
    recipes = User.read_recipes({"user_id": session["user"]["id"]})
    for recipe in recipes:
        if recipe["id"] == id:
            Recipe.delete_one({"recipe_id": id})
            break
    return redirect("/recipes")