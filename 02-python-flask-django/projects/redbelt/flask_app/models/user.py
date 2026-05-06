from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.pie import Pie
from flask import flash
import re
mydb = 'pypie_derby'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod # METHOD FOR INSERTING INTO USERS AND THATS IT
    def save(cls,data):
        query = ''' INSERT INTO users(first_name,last_name,email,password)VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);'''
        results = connectToMySQL(mydb).query_db(query,data)
        return results
    
    @classmethod # METHOD TO GET USERS BY ID
    def get_by_id(cls,data):
        query = ''' SELECT * FROM users WHERE id = %(id)s;'''
        results = connectToMySQL(mydb).query_db(query,data)
        print(results)
        return cls(results[0])

    @classmethod # METHOD TO GET USERS BY EMAIL
    def get_by_email(cls,data):
        query = '''SELECT * FROM users WHERE email = %(email)s;'''
        results = connectToMySQL(mydb).query_db(query,data)
        print(results)
        # IF DIDN'T FIND MATCHING USER
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod #dojoninja
    def get_one_pie(cls, data):
        query = """
        SELECT * FROM users LEFT JOIN pies on pies.baker_id = users.id WHERE pies.id = %(id)s; """
        results = connectToMySQL(mydb).query_db(query, data)
        if not results:
            print("WE HAVE NO RESULTS TO SHOW CONNECT TO MY SQL IS NOT WORKING")
            return []
        user = cls(results[0])
        for item in results:
            n = {
                    'id': item['pies.id'],
                    'name': item['name'],
                    'filling' : item['filling'],
                    'crust' : item['crust'],
                    'created_at' : item['created_at'],
                    'updated_at' : item['updated_at'],
                    'baker_id' : item['baker_id'],
                    'consumer_id' : item['consumer_id'],
                }
            user.pies.append(Pie(n))
            return user

    @staticmethod # STATIC METHOD FOR VALIDATIONS
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash('First name must be at least 3 letters long.', 'register')
            is_valid = False
        if not user['first_name'].isalpha():
            flash('First name can only contain letters.', 'register')
            is_valid = False
        if len(user['last_name']) < 3:
            flash('Last name must be at least 3 letters long.', 'register')
            is_valid = False
        elif not user['last_name'].isalpha():
            flash('Last name can only contain letters.', 'register')
            is_valid = False
        if len(user['email']) < 1:
            is_valid = False
            flash('Email required', 'register')
        elif not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address.', 'register')
            is_valid = False
        if len(user['password']) < 8:
            flash('Password must have at least 8 characters.', 'register')
            is_valid = False
        elif user['confirm_password'] != user['password']:
            flash('Passwords do not match.', 'register')
            is_valid = False
        this_user = User.get_by_email(user)
        if this_user:
            is_valid = False
            flash('Email already exists.', 'register')
        return is_valid