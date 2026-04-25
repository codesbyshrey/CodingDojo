from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

class Recipe:
    DB = "recipes"

    def __init__(self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.under = data["under"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (user_id, name, description, instructions, under) VALUES (%(user_id)s, %(name)s, %(description)s, %(instructions)s, %(under)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under=%(under)s WHERE id = %(recipe_id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.DB).query_db(query)
        if not results:
            return False
        recipes = []
        for result in results:
            recipes.append(cls(result))
        return recipes


    @classmethod
    def read_all_with_users(cls):
        query = "SELECT recipes.*, users.first_name, users.id AS user_id FROM recipes LEFT JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(cls.DB).query_db(query)
        if not results:
            return False
        recipes = []
        for result in results:
            recipes.append(cls(result))
        return recipes

    @classmethod
    def read_one_with_user(cls, data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return False
        return results[0]

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM recipes WHERE id = %(recipe_id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate(data):
        isValid = True
        print(data)
        print(data)
        if len(data["name"]) < 3:
            flash("Name must be more than 3 characters.")
            isValid = False
        if len(data["description"]) < 3:
            flash("Description must be more than 3 characters.")
            isValid = False
        if len(data["instructions"]) < 3:
            flash("Instructions must be more than 3 characters.")
            isValid = False
        if data["date"] == "":
            flash("You must select a date.")
            isValid = False
        if "under" not in data:
            flash("You must select whether its under 30 minutes or not.")
            isValid = False
        return isValid