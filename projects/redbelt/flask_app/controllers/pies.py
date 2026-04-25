from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models import pie

# ACTION ROUTE
@app.route('/add_pie', methods=['POST'])
def add_pie():
    if pie.Pie.validate_pie(request.form):
        data = {
            'name': request.form['name'],
            'filling': request.form['filling'],
            'crust': request.form['crust'],
            'baker_id': session['user_id']
        }
        print(data)
        pie.Pie.save(data)
        return redirect('/dashboard')
    return redirect('/dashboard')

# DISPLAY ROUTE
@app.route('/pies')
def show_pies():
    return render_template('pie_derby.html', pies = pie.Pie.get_all())

# DISPLAY ROUTE
@app.route('/show/<int:id>')
def pie_card(id):
    return render_template('pie_card.html', pie = pie.Pie.get_one({'id':id}))


# ACTION ROUTE SO IT REDIRECTS ################################################
@app.route('/like/<int:pie_id>', methods=['POST'])
def like(pie_id):
    data = {
        'id': pie_id,
        'consumer_id': session['user_id']
    }
    pie.Pie.like(data)
    return redirect(f'/show/{pie_id}')
    
@app.route('/dislike/<int:pie_id>', methods=['POST'])
def dislike(pie_id):
    data = {
        'id': pie_id
    }
    pie.Pie.dislike(data)
    return redirect(f'/show/{pie_id}')
###############################################################################

# DISPLAY ROUTE
@app.route('/edit/<int:id>')
def edit(id):
    return render_template('edit.html', this_pie = pie.Pie.get_one({'id': id}))

# ACTION ROUTE SO IT REDIRECTS ################################################
@app.route('/edit_pie/<int:id>', methods=['POST'])
def edit_pie(id):
    data = {
        'id' : id,
        'name': request.form['name'],
        'filling': request.form['filling'],
        'crust': request.form['crust']
    }
    pie.Pie.edit(data)
    return redirect('/dashboard')

# ACTION ROUTE WITH A REDIRECT #################################################
@app.route('/delete/<int:id>')
def delete(id):
    pie.Pie.delete({'id': id})
    return redirect('/dashboard')