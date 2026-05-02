from flask_app import app
from flask import render_template, session, request, redirect, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Display Route
@app.route('/')
def index():
     return render_template("index.html")

# Action Route
@app.route('/register', methods=['POST'])
def register():
     if not User.validate_register(request.form):
          return redirect("/")
     data = {
          'first_name': request.form['first_name'],
          'last_name' : request.form['last_name'],
          'email' : request.form['email'],
          'password' : bcrypt.generate_password_hash(request.form['password'])
     }
     id = User.create(data)
     session['user_id'] = id
     return redirect('/main')

@app.route("/login", methods=["POST"])
def login():
     user = User.get_by_email(request.form)

     if not user:
          flash("invalid email", "login")
          return redirect('/')
     if not bcrypt.check_password_hash(user.password, request.form['password']):
          flash("invalid password", "login")
          return redirect("/")
     session['user_id'] = user.id
     return redirect("/main")

@app.route('/main')
def main():
     if 'user_id' not in session:
          return redirect('/logout')
     data = {
          'id': session['user_id']
     }
     user = User.get_by_id(data)
     return render_template("show_all.html", user=user, recipes=Recipe.get_all())

@app.route('/logout')
def logout():
     session.clear()
     return redirect("/")