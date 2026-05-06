from flask_app import app
from flask import flash, render_template, request, redirect, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt( app )

@app.route('/' )
def display_login():
    return render_template('login.html')

@app.route( '/user/registration', methods = ['POST'] )
def process_registration():
    # Validate the registration form
    if User.validate_registration( request.form ) == False:
        return redirect( '/' )
    # Validate if the user already exists
    user_exists = User.get_one_to_validate_email( request.form )
    if user_exists != None:
        flash( "This email already exists!", "error_registration_email" )
        return redirect( '/' )
    # Proceed to create the user
    data = {
        **request.form,
        "password" : bcrypt.generate_password_hash( request.form['password'] )
    }
    user_id = User.create( data )

    session['first_name'] = data['first_name']
    session['email'] = data['email']
    session['user_id'] = user_id

    return redirect( '/recipes' ) # This needs to change to another display route

@app.route( '/user/login', methods = ['POST'] )
def process_login():
    current_user = User.get_one_to_validate_email( request.form )

    if current_user != None:
        if not bcrypt.check_password_hash( current_user.password, request.form['password'] ):
            flash( "Wrong credentials", "error_login_credentials" )
            return redirect( '/' )
        
        session['first_name'] = current_user.first_name
        session['email'] = current_user.email
        session['user_id'] = current_user.id
        
        return redirect( '/recipes' )
    else:
        flash( "Wrong credentials", "error_login_credentials" )
        return redirect( '/' )

@app.route( '/user/logout' )
def process_logout():
    session.clear()
    return redirect( '/' )