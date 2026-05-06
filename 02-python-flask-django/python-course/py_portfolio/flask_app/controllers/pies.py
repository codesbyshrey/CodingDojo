from flask import redirect, render_template, request, session, flash
from flask_app import app
from flask_app.models.pie import Pie
from flask_app.models.vote import Vote

# @app.route('/portfolio')
# def portfolio():
#     return render_template('index.html')

# @app.route("/portfolio/codesbyshrey")
# def codesbyshrey():
#     return render_template('codesbyshrey.html')

# @app.route("/portfolio/picsbyshrey")
# def picsbyshrey():
#     return render_template('picsbyshrey.html')

# @app.route("/portfolio/vidsbyshrey")
# def vidsbyshrey():
#     return render_template('vidsbyshrey.html')

#========================== Create New Recipe =========================
@app.route('/pie/create', methods=['POST'])
def create_new_recipe():
    if not Pie.validate_pie(request.form):
        return redirect('/dashboard')

    data = {
        'name': request.form['name'],
        'filling': request.form['filling'],
        'crust': request.form['crust'],
        'user_pie_id': session['user_id']
    }
    Pie.create_new_pie(data)

    return redirect('/dashboard')

#========================== Render Edit Page =========================
@app.route('/edit/<pie_id>')
def edit_pie_display(pie_id):
    if 'user_id' not in session:
        return redirect('/')

    data = {
        'pie_id': pie_id
    }
    pie = Pie.get_pie_info(data)


    return render_template('edit_candidate.html', pie = pie)

#========================== Apply edit to database  POST! =========================
@app.route('/edit/<pie_id>/post', methods=['POST'])
def edit_recipe(pie_id):

    if not Pie.validate_pie(request.form):
        return redirect(f'/edit/{pie_id}')

    data = {
        'name': request.form['name'],
        'filling': request.form['filling'],
        'crust': request.form['crust'],
        'pie_id': pie_id,
        'creator_id': session['user_id']
    }

    Pie.update_pie(data)


    return redirect('/dashboard')

#========================== Render Edit Page =========================
@app.route('/pies')
def view_pies():
    if 'user_id' not in session:
        return redirect('/')

    pies = Pie.get_all_pies()


    return render_template('election.html', pies = pies)


#========================== Render Pie View age =========================
@app.route('/show/<pie_id>/<creator_first>')
def display_pie(pie_id, creator_first):

    data={
        'pie_id': pie_id
    }
    pie = Pie.get_pie_info(data)

    datax = {
        'pie_id': pie_id,
        'voter_id': session['user_id']
    }
    user_voted = Vote.user_vote(datax)


    return render_template('show_candidate.html', pie = pie, user_voted = user_voted, creator_first = creator_first)





#========================== Render Delete method   POST! =========================
@app.route('/delete/<pie_id>')
def delete_recipe(pie_id):

    data = {
        'pie_id': pie_id
    }

    Pie.delete_pie(data)


    return redirect('/dashboard')


#===================== User vote for Pie ================
@app.route('/pie/vote/<pie_id>')
def make_vote(pie_id):

    data={
        'pie_id': pie_id,
        'voter_id': session['user_id']
    }
    
    Vote.create_vote(data)

    return redirect('/pies')


#====================== User unvote for pie=============
@app.route('/pie/unvote/<pie_id>')
def delete_vote(pie_id):

    data={
        'pie_id': pie_id,
        'voter_id': session['user_id']
    }
    
    Vote.delete_vote(data)

    return redirect('/pies')