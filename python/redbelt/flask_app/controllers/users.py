# no errors here, don't bother coming back to look

from flask_app import app
from flask import render_template, session, request, redirect, flash
from flask_app.models.user import User
from flask_app.models.pie import Pie
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Display Route
@app.route('/')
def index():
     if 'user_id' in session:
          return redirect('/dashboard')
     # if our user is already logged in, take them straight to the dashboard
     return render_template("loginreg.html")

# Action Route WITH A REDIRECT METHOD --> after registration, take them to dashboard
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
     # email validation check
     user = User.get_by_email(data)
     if user:
          flash("This email is already registered, please try with a different email or proceed to LOG IN", "register")
          return redirect('/')
     # if it's a new user, we now call the create class method to add them into our data table via our model. maybe consider more hyperspecific names
     id = User.create(data)
     session['user_id'] = id
     session['user_first_name'] = request.form['first_name']
     return redirect('/dashboard')

# ACTION ROUTE SO IT WILL REDIRECT FOR A USER WHO IS LOGGING IN
@app.route("/login", methods=["POST"])
def login():
     user = User.get_by_email(request.form)

     if not user:
          session.clear()
          flash("Invalid Email, not yet Registered", "login")
          return redirect('/')
     
     if not bcrypt.check_password_hash(user.password, request.form['password']):
          flash("Invalid Password, please try again. Check your email address to make sure it is inputted correctly", "login")
          return redirect("/")
     
     session['user_id'] = user.id
     session['user_first_name'] = user.first_name
     return redirect("/dashboard")

# DISPLAY ROUTE FOR CORRESPONDING ACTION ROUTE ABOVE
@app.route('/dashboard')
def main():
     if 'user_id' not in session:
          return redirect('/')
     data = {
          'id': session['user_id']
     }
     user = User.get_by_id(data)
     user_pies=Pie.get_all()
     print(user, user_pies)
     print('user_first_name')
     return render_template("dashboard.html", user=user, user_pies = user_pies)

@app.route('/logout')
def logout():
     session.clear()
     return redirect("/")