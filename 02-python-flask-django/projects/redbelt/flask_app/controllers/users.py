from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user, pie
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# DISPLAY ROUTE
@app.route('/')
def index():
    return render_template('index.html')

# ACTION ROUTE SO IT REDIRECTS #############################################
@app.route('/new', methods=['POST'])
def log_new_user():
    if user.User.validate_user(request.form):
        password = bcrypt.generate_password_hash(request.form['password'])
        print(password)
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': password
        }
        print(data)
        user_id = user.User.save(data)
        print(user_id)
        session['user_id'] = user_id
        return redirect('/dashboard')
    return redirect('/')

# DISPLAY ROUTE ONLY FOR THE IF STATEMENT, ONLY ACTION IS REDIRECTING
@app.route('/dashboard')
def recipes():
    if 'user_id' in session:
        data = {
            'id': session['user_id']
        }
        print(session['user_id'])
        return render_template('dashboard.html', this_user = user.User.get_by_id(data), this_user_pies = pie.Pie.get_by_id(data))
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    this_user =user.User.get_by_email(request.form)
    print(request.form)
    if this_user:
        if bcrypt.check_password_hash(this_user.password, request.form['password']):
            session['user_id'] = this_user.id
            return redirect ('/dashboard')
    flash('Invalid credentials!', 'login')
    return redirect ('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')