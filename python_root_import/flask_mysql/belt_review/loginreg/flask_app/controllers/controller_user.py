from flask_app import app
from flask import render_template, session, request, redirect, flash
from flask_app.models.model_user import User
from flask_bcrypt import Bcrypt

# find out why this and mypysql.cursors show up with yellow underlines for you. Everything works just fine, so probably some issue with an extension that's being extra nitpicky.

# Review Bcrypt way more. Implementation / putting in the code and where to put in makes sense to me. Maybe I'm overcomplicating it the same way I did with Flask. But something about it feels uneasy. Get it fixed.

bcrypt = Bcrypt(app)

@app.route('/')
def index():
     return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
     if not User.validate_register(request.form):
          return redirect('/')
     data = {
          'first_name' : request.form['first_name'],
          'last_name' : request.form['last_name'],
          'email' : request.form['email'],
          'password' : bcrypt.generate_password_hash(request.form['password'])
     }
     id = User.create(data)
     session['user_id'] = id
     return redirect('/main')


@app.route('/login', methods=['POST'])
def login():
     user = User.get_by_email(request.form)

     if not user:
          flash(" Email is Invalid","Login")
          return redirect('/')
     if not bcrypt.check_password_hash(user.password, request.form['password']):
          flash(" Password is Invalid","Login")
          return redirect('/')
     session['user_id'] = user.id
     return redirect('/main')


@app.route('/main')
def main():
     if 'user_id' not in session:
          return redirect('/logout')
     data = {'id': session['user_id']}
     user = User.get_by_id(data)
     return render_template("login.html", user = user )

@app.route('/logout')
def logout():
     session.clear()
     return redirect('/')