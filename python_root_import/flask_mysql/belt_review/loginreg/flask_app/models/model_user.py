from flask_app.config.mysqlconnection import connectToMySQL
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

# Brush back up on Learn with REGEX and re. Definitely didn't pay enough attention to be able to intuitively understand / remember to do it and don't want to pay the price on exam day by uselessly hunting through the Learn Platform. Get to a state of pseudocoding / mapping out these ideas in English on paper and pencil.

class User:
     def __init__(self, data):
          self.id = data["id"]
          self.first_name = data["first_name"]
          self.last_name = data["last_name"]
          self.email = data["email"]
          self.password = data["password"]
          self.created_at = data["created_at"]
          self.updated_at = data["updated_at"]

     # Make sure you have the schema name correct in the connect parantheses dork, otherwise it'll never figure out which file you're even trying to connect to. Messed that up on dojos_ninjas too because you were blindly working w/ the group and called it dojos_and_ninjas. Either that or just start naming stuff strictly like it is on the Learn Platform lol

     # Get some more validation regarding where to save the schemas relative to your folders in the file structure. It shouldn't be important, but worth looking into to make sure you understand why it isn't important.

     @classmethod
     def get_all(cls):
          query = "SELECT * FROM users;"
          results = connectToMySQL("user_loginreg").query_db(query)

          # THIS IS A HUGELY IMPORTANT STEP DO NOT FORGET IT
          # ALLOWS US TO ITERATE OVER NEW ARRAY THAT WE CAN CHANGE VALUES INSIDE, COMPARED TO OUR IMMUTABLEMULTIDICT
          # after the exam pls god make a single reference basis for this lol

          all_users = []
          for user in results:
               all_users.append( cls(user) )
          return all_users

     @classmethod
     def create(cls, data):
          query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
          return connectToMySQL("user_loginreg").query_db(query, data)

     @classmethod
     def get_by_email(cls, data):
          query = "SELECT * FROM users WHERE email = %(email)s;"
          results = connectToMySQL("user_loginreg").query_db(query,data)
          if len(results) < 1:
               return False
          return cls(results[0])

     @classmethod
     def get_by_id(cls, data):
          query = "SELECT * FROM users WHERE id = %(id)s;"
          results = connectToMySQL("user_loginreg").query_db(query, data)
          return cls(results[0])

     # Could probably copy paste this more or less for the exam in case we have login based validation stuff to check off for. Just have to make sure the database names and reinstantiation of the class names are appropriately the same for the pertinent assignment.

     @staticmethod
     def validate_register(user):
          is_valid = True
          if not EMAIL_REGEX.match(user['email']):
               flash("Email Addres is Invalid","Register")
               is_valid = False
          if len(user["first_name"]) < 3:
               flash("First Name should be 3 characters minimum","REGISTER")
               is_valid= False
          if len(user["last_name"]) < 3:
               flash("Last Name should be 3 characters minimum","REGISTER")
               is_valid= False
          if len(user["password"]) < 4:
               flash("Password should be 4 characters minimum","REGISTER")
               is_valid= False
          if user["password"] != user["confirm"]:
               flash("Passwords Do NOT Match","REGISTER")
               is_valid= False
          return is_valid
     
# if you're desperate enough to come back here to reference for the exam, GOOD LUCK FUTURE SHREYAS YOU GOT THIS BELIEVE IN YOURSELF AND FULL SEND