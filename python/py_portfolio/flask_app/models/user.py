from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session
import re

first_name_regex = re.compile(r'^[A-Z][a-zA-Z- ]+$')
last_name_regex = re.compile(r'^[A-Z][a-zA-Z- ]+$')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
password_regex = re.compile(r'^[a-zA-Z0-9-.\/\\#@!$%^&*]{8,20}')

DATABASE = "voting_db"

class User():
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_register(user):
        is_valid = True

        if len(user['first_name']) < 2:
            is_valid = False
            flash("Invalid First Name entry!", "register")
        elif not first_name_regex.match(user['first_name']):
            flash("Make sure to capitalize first letter.", "register")
            is_valid = False

        if len(user['last_name']) < 3:
            is_valid = False
            flash("Invalid Last Name entry!", "register")
        elif not last_name_regex.match(user['last_name']):
            flash("Make sure to capitalize first letter.", "register")
            is_valid = False

        if not email_regex.match(user['email']):
            flash("Invalid email address!", "register")
            is_valid = False

        if not (user['password']) == (user['password_confirm']):
            flash('Passwords do not match!', "register")
            is_valid - False
        
        if len(user['password']) < 8 or len(user['password']) > 20:
            is_valid = False
            flash('Password length is an issue!', "register")
        elif not password_regex.match(user['password']):
            flash('Password contains unsupported characters')
        return is_valid

# ======================= Create New User =================================

    @classmethod
    def create_user(cls, data):

        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)'

        results = connectToMySQL(DATABASE).query_db(query, data)

        return results


# =======================    Get User information       =================================

    @classmethod
    def get_user_info(cls, data):

        query = "SELECT * FROM users WHERE id = %(user_id)s;"

        return connectToMySQL(DATABASE).query_db(query, data)


# =======================    Get User information  by Email ========================

    @classmethod
    def get_by_email(cls, data):

        query = "SELECT * FROM users WHERE email = %(email)s"

        return connectToMySQL(DATABASE).query_db(query, data)