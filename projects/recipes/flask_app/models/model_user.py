from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "recipes"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def read_recipes(cls, data):
        query = "SELECT recipes.id,recipes.user_id FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE recipes.user_id = %(user_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return False
        recipes = []
        for result in results:
            recipes.append(cls(result))
        return recipes


    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    @staticmethod
    def validate_login(data):
        isValid = True
        if not User.read_one(data):
            flash("User not found with those credentials.")
            isValid = False
        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address format!")
            isValid = False
        if len(data["email"]) < 1:
            flash("Enter an email.")
            isValid = False
        if len(data["password"]) < 1:
            flash("Enter a password.")
            isValid = False
        return isValid

    @staticmethod
    def validate_create(data):
        isValid = True
        if User.read_one(data):
            flash("Email already exists!")
            isValid = False
        if len(data["fname"]) < 2:
            flash("Your first name must be greater than 2 characters.")
            isValid = False
        if len(data["lname"]) < 2:
            flash("Your last name must be greater than 2 characters.")
            isValid = False
        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address!")
            isValid = False
        if len(data["password"]) < 8:
            flash("Your password must be at least 8 characters.")
            isValid = False
        if data["password"] != data["confirm-password"]:
            flash("Passwords must match.")
            isValid = False
        return isValid