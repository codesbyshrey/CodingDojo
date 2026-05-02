# This file should stay outside of the flask_app file
# Run this file after the pipenv shell is created

from flask_app.controllers import controllers_users
from flask_app import app

if __name__ =="__main__":
     app.run(debug=True)