from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/new/recipe')
def new_recipe():
     if 'user_id' not in session:
          return redirect('/logout')
     data = {
          "id": session['user_id']
     }
     return render_template('add_recipe.html', user=User.get_by_id(data))

@app.route('/create/recipe', methods=['POST'])
def create_recipe():
     if 'user_id' not in session:
          return redirect('/new/recipe')
     if not Recipe.validate_recipe(request.form):
          return redirect('/new/recipe')
     data = {
          "name": request.form["name"],
          "description": request.form["description"],
          "instruction": request.form["instruction"],
          "date_cooked": request.form["date_cooked"],
          "under": request.form["under"],
          "user_id": session["user_id"]
     }
     Recipe.create(data)
     return redirect("/main")

@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
     if 'user_id' not in session:
          return redirect('/logout')
     data = {
          "id":id
     }
     user_data = {
          "id":session['user_id']
     }
     return render_template("edit_recipe.html", edit=Recipe.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/recipe',methods=['POST'])
def update_recipe():
     if 'user_id' not in session:
          return redirect('/logout')
     if not Recipe.validate_recipe(request.form):
          return redirect('/main')
     data = {
          "name": request.form["name"],
          "description": request.form["description"],
          "instruction": request.form["instruction"],
          "date_cooked": request.form["date_cooked"],
          "under": request.form["under"],
          "id": request.form['id']
     }
     Recipe.update(data)
     return redirect('/main')

@app.route('/recipe/<int:id>')
def show_recipe(id):
     if 'user_id' not in session:
          return redirect('/logout')
     data = {
          "id":id
     }
     user_data = {
          "id":session['user_id']
     }
     return render_template("show_one.html",recipe=Recipe.get_one(data),user=User.get_by_id(user_data))

@app.route('/delete/recipe/<int:id>')
def delete_recipe(id):
     if 'user_id' not in session:
          return redirect('/logout')
     data = {
          "id":id
     }
     Recipe.delete(data)
     return redirect('/main')