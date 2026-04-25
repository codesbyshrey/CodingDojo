from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

DB = "pie_derby" # this lets me just throw in DB anytime I need the connectToMySQL so I stop confusing myself in silly ways

# Establishing our recreated instance as a list of dictionaries we can edit, calling upon it like a class to interact with our database via queries.

class Pie:
     def __init__(self, data):
          self.id = data["id"]
          self.name = data["pie_name"]
          self.filling = data["filling"]
          self.crust = data["crust"]
          self.user_pie_id = data["user_pie_id"]
          self.votes = data['votes'] # new lines so that we can interact with the voting data as we need it
          self.user_first = ['first_name'] # needed on the derby page to allow user names to correspond with votes on table properly
          self.created_at = data["created_at"]
          self.updated_at = data["updated_at"]

##### CLASS METHODS ARE HERE ########
     @classmethod
     def create(cls, data):
          query = "INSERT INTO pies (pie_name, filling, crust, user_pie_id) VALUES (%(name)s,%(filling)s,%(crust)s,%(user_pie_id)s);"
          results = connectToMySQL(DB).query_db(query,data)
          return results

# Geting all pies (different from all pies for a user) - need to JOIN here like in dojos and ninjas so that we can properly display all the pies on our Derby page
     @classmethod
     def get_all(cls):
          query = " SELECT pies.id, pies.pie_name, users.first_name, COUNT(votes.id) AS votes FROM pies JOIN users ON pies.user_pie_id = users.id LEFT JOIN votes ON pies.id = votes.pie_id GROUP BY pies.id ORDER BY votes DESC;"
          results = connectToMySQL(DB).query_db(query)
          all_pies = []
          # pulled from dojos and ninjas as the tip Tbo gave Tyrik prior to starting exam
          if not results:
               return []
               # if this query comes back as a false value or empty list it prevents the run. put it in all of your class methods after the results so it doesn't continue breaking your code
          for rec in results:
               print(rec['name'])
               all_pies.append( cls(rec) )
          return all_pies

# Get all pies for A SPECIFIC USER to keep updating dashboard page as recipes are added as needed
     @classmethod
     def get_user_pie(cls, data):
          print (data) # double check in terminal to make sure you're pulling the correct information
          query = "SELECT * FROM pies WHERE user_pie_id = %(;user_id)s;"
          results = connectToMySQL(DB).query_db(query, data)
          user_pies = []
          if not results:
               return []
               # if this query comes back as a false value or empty list it prevents the run. put it in all of your class methods after the results so it doesn't continue breaking your code
          for rec in results:
               print(rec['first_name']) # making sure we're getting the pies for the right user, peep terminal
               user_pies.append( cls(rec) )
          return user_pies

# GET a pie's information for the autopopulate areas 
     @classmethod
     def get_one_pie(cls, data):
          query = "SELECT * FROM pies WHERE pies.id = %(pie_id)s;"
          results = connectToMySQL(DB).query_db(query, data)
          pie_info = []
          for rec in results:
               print(rec['name'])
               pie_info.append( cls(rec) )
          print (pie_info) #check in terminal
          return pie_info #added the indexed at zero because on the vote page we only want to see the immediate pie that we are accessing

# UPDATE A PIE --> attached to the edit buttons
     @classmethod
     def update_pie(cls, data):
          query = "UPDATE pies SET pie_name=%(pie_name)s, filling=%(filling)s, crust=%(crust)s, updated_at=NOW() WHERE id = %(id)s;"
          return connectToMySQL(DB).query_db(query, data)

# DELETE A PIE
     @classmethod
     def delete_pie(cls, data):
          query = "DELETE FROM pies WHERE id = %(id)s;"
          return connectToMySQL(DB).query_db(query, data)


###### STATIC METHOD TO VALIDATE OUR PIES AND FLASH ERRORS AS NEEDED #######
     @staticmethod
     def validate_pie(pie):
          is_valid = True
          if len(pie["name"]) < 2:
               flash("Name can't be left blank, more than 2 characters please","pie")
               is_valid= False

          if len(pie["filling"]) < 2:
               flash("Filling can't be left blank, more than 2 characters please","pie")
               is_valid= False

          if len(pie["crust"]) < 2:
               flash("Crust can't be left blank, more than 2 characters please","pie")
               is_valid= False

          return is_valid