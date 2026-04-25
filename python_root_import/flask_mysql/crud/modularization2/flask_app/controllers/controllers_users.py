from flask_app import app
from flask import render_template, session, request, redirect
from flask_app.models.model_user import User

# Default App Page
@app.route('/')
def index():
     return redirect('/user')

# Rendering the Index Page
@app.route('/user')
def index():
     return render_template('index.html', users=User.get_all())

# Showing New User Page with function to Add User
@app.route('/user/new')
def add_user():
     return render_template('new_user.html')

# Create User Function to POST to Database
@app.route('/user/create', methods=['POST'])
def create_user():
     print(request.form)
     User.save(request.form)
     return redirect('/user')

# Showing Selected User w/ corresponding ID in URL Link
@app.route('/user/showone/<int:id>')
def show_one(id):
     data = {
          "id":id
     }
     return render_template('show_user.html', user=User.show_one(data))

# Showing Selected User w/ Ability to Edit User, corresponding ID in URL
@app.route('/user/edit/<int:id>')
def edit_user(id):
     data = {
          "id":id
     }
     return render_template('edit_user.html', user=User.show_one(data))

# Updating User Page to POST to database and UPDATE the form
@app.route('/user/update', methods=['POST'])
def update_user():
     User.update(request.form)
     return redirect('/user')

# Page to Delete the User (still in progress)
@app.route('/user/delete/<int:id>')
def delete_user(id):
     data = {
          "id":id
     }
     return redirect('/user')

# Actually DELETING the user and POST to DB to ensure User goes Kaput
@app.route('/user/delete', methods=['POST'])
def delete():
     User.delete(request.form)
     return redirect('/user')