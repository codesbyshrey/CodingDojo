from sqlite3 import DatabaseError
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.user import User

from flask import flash, session

DATABASE = "voting_db"

class Pie():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        if 'filling' in data:
            self.filling = data['filling']
        if 'crust' in data:
            self.crust = data['crust']
        if 'created_at' in data:
            self.created_at = data['created_at']
        if 'updated_at' in data:
            self.updated_at = data['updated_at']
        if 'user_pie_id' in data:
            self.user_pie_id = data['user_pie_id']
        if 'first_name' in data:
            self.user_first = data['first_name']
        if 'votes' in data:
            self.votes = data['votes']

    @staticmethod
    def validate_pie(pie):
        is_valid = True

        if len(pie['name']) <= 2:
            is_valid = False
            flash("Pie name is not long enough!")
        if len(pie['filling']) <= 2:
            is_valid = False
            flash("Filling is not long enough!")
        if len(pie['crust']) <= 2:
            is_valid = False
            flash("Crust are not long enough!")
        return is_valid
#======================== GetAll Pies for Display ==============

    @classmethod
    def get_all_pies(cls):
        
        query = "SELECT pies.id, pies.name, users.first_name, COUNT(votes.id) as votes FROM pies JOIN users ON pies.user_pie_id = users.id LEFT JOIN votes ON pies.id = votes.pie_id GROUP BY pies.id ORDER BY votes DESC;"
        results = connectToMySQL(DATABASE).query_db(query)

        pies = []

        for item in results:
            pies.append(cls(item))
            print(item);
        return pies

#======================== GetAll Pies created by User ==============

    @classmethod
    def get_pie_byid(cls, data):
        
        print(data)
        query = "SELECT * FROM pies WHERE user_pie_id = %(user_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        pies = []


        for item in results:
            pies.append(cls(item))

        return pies


#======================== Get pie information ==============

    @classmethod
    def get_pie_info(cls, data):
        
        query = "SELECT * FROM pies WHERE pies.id = %(pie_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        pie = []
        

        for item in results:
            pie.append(cls(item))
        print(pie)
        return pie[0]


#========================== Create a New Recipe =====================

    @classmethod
    def create_new_pie(cls, data):

        query = "INSERT INTO pies (name, filling, crust, created_at, updated_at, user_pie_id) VALUES (%(name)s, %(filling)s, %(crust)s, NOW(), NOW(), %(user_pie_id)s);"

        results = connectToMySQL(DATABASE).query_db(query, data)

        return results


#========================== Update Recipe ====================
    @classmethod
    def update_pie(cls, data):

        query =  "UPDATE pies SET name = %(name)s, filling = %(filling)s, crust = %(crust)s WHERE id = %(pie_id)s;"

        connectToMySQL(DATABASE).query_db(query, data)

        return



#========================== Delete Recipe =====================
    @classmethod
    def delete_pie(cls, data):

        query1 = "DELETE FROM votes WHERE pie_id = %(pie_id)s"
        query2 = "DELETE FROM pies WHERE id = %(pie_id)s"


        connectToMySQL(DATABASE).query_db(query1, data)
        connectToMySQL(DATABASE).query_db(query2, data)

        return