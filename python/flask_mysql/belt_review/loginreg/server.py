from flask_app import app
from flask_app.controllers import controller_user

# In dojos and ninjas we had multiple controllers, here we only have 1. Don't forget to import all the controllers in the exam file in case you come back here for referencing

if __name__ =="__main__":
     app.run(debug=True)