#cls - accepts the class as a PARAMETER rather than an OBJECT OR INSTANCE (classmethod)
# From the flask app, we import connectToMySQL function
     # that function receives the database we're using and creates an instance of it, which is why we can interact with the classes and queries via class methods directly here

from flask_app.configmysqlconnection import connectToMySQL

class User:
     # Initialize the Data we need
     def __init__(self, data):
          self.id = data["id"]
          self.first_name = data["first_name"]
          self.last_name = data["last_name"]
          self.email = data["email"]
          self.created_at = data["created_at"]
          self.updated_at = data["updated_at"]

     # Full Name
     def full_name(self):
          return f"{self.first_name} {self.last_name}" 

     # Class Method to Get All, and adjust as a list of dictionaries
     @classmethod
     def get_all(cls):
          query = "SELECT * FROM users;"
          results = connectToMySQL('users_schema').query_db(query)
          users = []
          for userX in results:
               users.append( cls(userX) )
          return users 

     # Inserting our Values when we need to add people
     @classmethod
     def save(cls, data):
          query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
          result = connectToMySQL("users_schema").query_db(query, data)
          return result

     # Being able to show a single person based on the id we select (reflected in URL on controller side)
     @classmethod
     def show_one(cls, data):
          query = "SELECT * FROM users WHERE id = %(id)s;"
          result = connectToMySQL("users_schema").query_db(query, data)
          return cls(result[0])
     
     # create a show_all class method SELECT * FROM users (without id ^^) CODE REVIEW INFORMATION

     # Update Method Dependent on ID
     @classmethod
     def update(cls, data):
          query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
          return connectToMySQL('users_schema').query_db(query, data)

     # Delete Method Dependent on ID
     @classmethod
     def delete(cls, data):
          query = "DELETE FROM users WHERE id=%(id)s;"
          return connectToMySQL('users_schema').query_db(query, data)