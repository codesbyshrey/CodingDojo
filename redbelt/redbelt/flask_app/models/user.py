# THIS MODEL INTERACTS WITH THE USERS SIDE OF OUR DATABASE IN ORDER TO UPDATE AND QUERY IT. THIS MODEL FILE IS PRETTY MUCH CONCRETE

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Establishing our recreated instance as a list of dictionaries we can edit, calling upon it like a class to interact with our database via queries.

DB = "pie_derby"

class User:
     def __init__ (self, data):
          self.id = data["id"]
          self.first_name = data["first_name"]
          self.last_name = data["last_name"]
          self.email = data["email"]
          self.password = data["password"]
          self.created_at = data["created_at"]
          self.updated_at = data["updated_at"]
     # FINISHED ABOVE DON'T TOUCH
###############################################

# class method to create new user
     @classmethod
     def create(cls, data):
          query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
          return connectToMySQL(DB).query_db(query,data)

# class method to get all users (tyler gave tyrik a tip before we went into exams, hunt down dojos_ninjas where you made note of it)
     @classmethod
     def get_all(cls):
          query = "SELECT * FROM users;"
          results = connectToMySQL(DB).query_db(query)
          all_users = []
          # this is a super crucial step that you cannot skip, it allows us to recreate the immutablemultidict as a list of dictionaries that we can actually have access to and append
          for user in results:
               all_users.append( cls(user) )
          print(all_users) # check in terminal
          return all_users

# class method to get user information by id
     @classmethod
     def get_by_id(cls, data):
          query = "SELECT * FROM users WHERE id = %(id)s;"
          results = connectToMySQL(DB).query_db(query, data)
          print(results) # check in terminal
          return cls(results[0])
     
# class method to get user information by email
     @classmethod
     def get_by_email(cls, data):
          query = "SELECT * FROM users WHERE email = %(email)s;"
          results = connectToMySQL(DB).query_db(query, data)
          if len(results) < 1:
               return False # this ensures we have emails available
          print(results) # check in terminal
          return cls(results[0])


##### STATIC METHOD FOR VALIDATION AND FLASH CHECKS ############
     @staticmethod
     def validate_register(user):
          is_valid = True
          if not EMAIL_REGEX.match(user['email']):
               flash("Invalid email address!","register")
               is_valid = False

          if len(user["first_name"]) < 3:
               flash("First name must be at least 3 characters!","register")
               is_valid= False

          if len(user["last_name"]) < 3:
               flash("Last name must be at least 3 characters!","register")
               is_valid= False

          if user["password"] != user["confirm"]:
               flash("Passwords don't match! Type carefully!","register")
               is_valid= False

          return is_valid