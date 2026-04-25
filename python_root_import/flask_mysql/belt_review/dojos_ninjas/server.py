from flask_app import app
from flask_app.controllers import dojos, ninjas

if __name__ == "__main__":
     app.run(debug=True)

# in MVC, the server calls on the controllers
# depending on ROUTE, controllers talk to models
# models use PyMySQL to talk to database and send CRUD queries
# models return back to controller w/ a recreated object
# controller routes back to templates for DOM