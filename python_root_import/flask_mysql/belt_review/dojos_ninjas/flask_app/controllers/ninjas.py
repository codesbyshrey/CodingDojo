from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
     return render_template('ninja.html', dojos = dojo.Dojo.get_all())

@app.route('/create/ninja', methods = ['POST'])
def create_ninja():
     ninja.Ninja.save(request.form)
     return redirect('/')

# Dojos provide most of the interaction
# In Ninjas, we only care about rendering profile page and redirecting new information with POST