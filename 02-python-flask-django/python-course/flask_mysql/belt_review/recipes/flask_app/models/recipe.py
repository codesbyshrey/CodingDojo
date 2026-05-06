from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
     def __init__(self, data):
          self.id = data["id"]
          self.name = data["name"]
          self.description = data["description"]
          self.instruction = data["instruction"]
          self.date_cooked = data["date_cooked"]
          self.under = data["under"]
          self.user_id = data["user_id"]
          self.created_at = data["created_at"]
          self.updated_at = data["updated_at"]

     @classmethod
     def create(cls, data):
          query = "INSERT INTO recipes (name, description, instruction, date_cooked, under, user_id) VALUES (%(name)s,%(description)s,%(instruction)s,%(date_cooked)s,%(under)s,%(user_id)s);"
          return connectToMySQL("recipes_index").query_db(query,data)

     @classmethod
     def get_all(cls):
          query = "SELECT * FROM recipes;"
          results = connectToMySQL("recipes_index").query_db(query)

          all_recipes = []
          for rec in results:
               print(rec['date_cooked'])
               all_recipes.append( cls(rec) )
          return all_recipes

     @classmethod
     def get_one(cls, data):
          query = "SELECT * FROM recipes WHERE id = %(id)s;"
          results = connectToMySQL("recipes_index").query_db(query, data)
          return cls(results[0])

     @classmethod
     def update(cls, data):
          query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instruction=%(instruction)s, date_cooked=%(date_cooked)s,under=%(under)s, updated_at=NOW() WHERE id = %(id)s;"
          return connectToMySQL("recipes_index").query_db(query, data)

     @classmethod
     def delete(cls, data):
          query = "DELETE FROM recipes WHERE id = %(id)s;"
          return connectToMySQL("recipes_index").query_db(query, data)

     @staticmethod
     def validate_recipe(recipe):
          is_valid = True
          if len(recipe["name"]) < 1:
               flash("Name can't be blank","recipe")
               is_valid= False
          if len(recipe["description"]) < 1:
               flash("Description can't be blank","recipe")
               is_valid= False
          if len(recipe["instruction"]) < 1:
               flash("Instruction can't be blank","recipe")
               is_valid= False
          if recipe['date_cooked'] == "":
               is_valid= False
               flash("missing date","recipe")
          return is_valid