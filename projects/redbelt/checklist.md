# Red Belt Exam: 2.24 Friday

 - Display Routes vs Action Routes (often POST, redirect not render)
 - print(request.form) and spam print in terminal as needed

```py
session['user_details'] = {
     'first_name' : request.form['first_name']
     'last_name' : request.form['last_name']
     'age' : request.form['age']
}
# This is just a simple way to remember and reassign your session details to form inputs. The principle will be the same in your models when you redefine and initialize your database table as a CLASS
```

## Steps To Take FOR EXAM WIREFRAME
LABEL DONE IN FRONT OF CHECKLIST ONCE FINISHED COMPLETELY. DON'T GO TO THE NEXT STEP WITHOUT EACH FIRST STEP BEING DONE, YOU TRY AND JUMP THINGS TOO OFTEN. SLOW AND STEADY BUDDY. 

## Checklist Items:
1. File Organization
2. Install flask, pymysql, flask-bcrypt
3. from flask import flash + import re for REGEX
4. Create ERD and Database, Link as needed + FORWARD ENGINEER (SINGULAR FOREIGN KEYS)
5. In models, declare DB = "name_of_database" to make it simple
6. Just immediately establish Bootstrap functionality
7. SERVER talks to CONTROLLERS who establishes ROUTES to RETURN / QUERY MODELS who interact with DATABASE who return to CONTROLLERS who ROUTE to TEMPLATES + STATIC

### mysqlconnection.py
```py
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
     def __init__(self, db):
          # change the user and password as needed
          connection = pymysql.connect(
                    host = 'localhost',
                    user = 'root', 
                    password = 'root',
                    # Mac is rootroot
                    db = db,
                    charset = 'utf8mb4',
                    cursorclass = pymysql.cursors.DictCursor,
                    autocommit = True)
          # establish the connection to the database
          self.connection = connection
     # the method to query the database
     def query_db(self, query, data=None):
          with self.connection.cursor() as cursor:
               try:
                    query = cursor.mogrify(query, data)
                    print("Running Query:", query)
     
                    cursor.execute(query)
                    if query.lower().find("insert") >= 0:
                         # INSERT queries will return the ID NUMBER of the row inserted
                         self.connection.commit()
                         return cursor.lastrowid
                    elif query.lower().find("select") >= 0:
                         # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                         result = cursor.fetchall()
                         return result
                    else:
                         # UPDATE and DELETE queries will return nothing
                         self.connection.commit()
               except Exception as e:
                    # if the query fails the method will return FALSE
                    print("Something went wrong", e)
                    return False
               finally:
                    # close the connection
                    self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
     return MySQLConnection(db)
```

### server.py
```py
from flask_app import app
from flask_app.controllers import #insert controller names here

if __name__ == "__main__":
     app.run(debug=True)

# in MVC, the server calls on the controllers
# depending on ROUTE, controllers talk to models
# models use PyMySQL to talk to database and send CRUD queries
# models return back to controller w/ a recreated object
# controller routes back to templates for DOM
```

### __init__.py
```py
from flask import Flask
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"
```

### Controllers Import
```py
from flask_app import app
from flask import render_template, session, request, redirect, flash
from flask_app.models.model_user import User
from flask_bcrypt import Bcrypt
```

### Models Import
```py
from flask_app.config.mysqlconnection import connectToMySQL
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash
```

### Templates Import
```HTML
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/ iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
     <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
```