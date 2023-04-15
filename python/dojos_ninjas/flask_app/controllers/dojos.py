from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
     return redirect('/dojos')

@app.route('/dojos')
def dojos():
     dojos = Dojo.get_all()
     return render_template('index.html', all_dojos = dojos)

# Action Route (POST - redirect)
@app.route('/create/dojo', methods=['POST'])
def create_dojo():
     Dojo.save(request.form)
     return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
     data = {'id': id}
     getNinja = Dojo.get_oneNinja(data)
     print(getNinja)
     return render_template('dojo.html', dojo=getNinja)

@app.route('/dojo/delete/<int:id>')
def delete_dojo(id):
     data = {'id':id}
     Dojo.delete(data)
     return redirect('/dojos')

#Controllers ROUTE to the pages after receiving the information from our models - which are our instantiated database copies