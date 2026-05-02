from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.pie import Pie
from flask_app.models.user import User
from flask_app.models.vote import Vote

""" THIS WAS COPIED OVER FROM RECIPES BUT I DON'T ACTUALLY NEED IT SINCE DASHBOARD HOLDS BOTH PAGES AT ONCE

# DISPLAY ROUTE SO WE RENDER TEMPLATE EDIT URLS
@app.route('/dashboard') 
def new_pie():
     if 'user_id' not in session:
          return redirect('/logout')
     data = {
          "id": session['user_id']
     }
     return render_template('dashboard.html', user=User.get_by_id(data))
"""

# ACTION ROUTE TO CREATE A PIE, WILL BE ON DASHBOARD
@app.route('/pie/create', methods=['POST']) #part of dashboard page now
def create_pie():
     if 'user_id' not in session:
          return redirect('/')
     if not Pie.validate_pie(request.form):
          return redirect('/dashboard')
     
     data = {
          "name": request.form["name"],
          "filling": request.form["filling"],
          "crust": request.form["crust"],
          "user_id": session["user_id"]
     }
     # consider making more hyperspecific function names in your models
     Pie.create(data)
     return redirect("/dashboard")
     # REDIRECT TO A DISLAY ROUTE, TRY AND KEEP IT RIGHT BELOW FOR EASE OF UNDERSTANDING YOUR OWN FILES



# DISPLAY ROUTE TO EDIT A PIE
@app.route('/edit/<pie_id>')
def edit_pie(pie_id):
     if 'user_id' not in session:
          return redirect('/')
     data = {
          "pie_id":pie_id
     }
     user_data = {
          "id":session['user_id']
     }
     return render_template("edit.html", edit=Pie.get_one_pie(data),user=User.get_by_id(user_data))



# ACTION ROUTE SO THIS WILL MOSTLY REDIRECT
@app.route('/edit/pie',methods=['POST'])
def update_pie(pie_id):
     if 'user_id' not in session:
          return redirect('/logout')
     if not Pie.validate_pie(request.form):
          return redirect(f'edit/{pie_id}')
     
     data = {
          "name": request.form["name"],
          "filling": request.form["filling"],
          "crust": request.form["crust"],
          "id": request.form['id']
     }

     Pie.update_pie(data)
     return redirect('/dashboard')


# DISPLAY ROUTE WITH POTENTIAL REDIRECTS
@app.route('/pies')
def show_pie():
     if 'user_id' not in session:
          return redirect('/')
     user_data = {
          "id":session['user_id']
     }
     pies = Pie.get_all()
     return render_template("derby.html", pies = pies, user=User.get_by_id(user_data))


# DISPLAY ROUTE TO RENDER A PIE FOR THE VOTING PAGE
@app.route('/show/<pie_id>')
def show_vote_pie(pie_id):
     data = {
          'pie_id':pie_id
     }
     pie = Pie.get_one_pie(data)

     # in here is likely where we figure out if a user has voted already, implement only if you have the time to do so
     
     return render_template('voting.html', pie = pie)

# ACTION ROUTE WITHOUT POST, STAY ON PAGE TECHNICALLY
@app.route('/delete/<pie_id>')
def delete_pie(pie_id):
     if 'user_id' not in session:
          return redirect('/')
     data = {
          "pie_id":pie_id
     }
     Pie.delete_pie(data)
     return redirect('/dashboard')