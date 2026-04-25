from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
mydb = 'pypie_derby'


class Pie:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.filling = data['filling']
        self.crust = data['crust']

        self.baker_id = data['baker_id'] #user who created --> can assign within function as needed specificaly for creation
        self.consumer_id = data['consumer_id'] # user who voted --> can assign votes to everyone as needed (i think this was black belt wireframe from what I remember) --> should allow me to track votes / take back votes
        self.votes = data['votes']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod # INSERT QUERY TO SAVE DATA
    def save(cls,data):
        query = '''INSERT INTO pies(name,filling,crust,baker_id) VALUES (%(name)s,%(filling)s,%(crust)s,%(baker_id)s);'''
        results = connectToMySQL(mydb).query_db(query,data)
        return results
    
    @classmethod # METHOD TO UPDATE LIKES
    def like(cls,data):
        query = ''' UPDATE pies SET votes = votes + 1,consumer_id = %(consumer_id)s WHERE id = %(id)s;'''
        results = connectToMySQL(mydb).query_db(query,data)
        return results

    @classmethod # METHOD TO REMOVE A LIKE / YUCKY - BLACK BELT CRITERIA ADDED AFTER RED BELT CRITERA WAS MET
    def dislike(cls,data):
        query = '''UPDATE pies SET votes = votes - 1,consumer_id = NULL WHERE id = %(id)s;'''
        results = connectToMySQL(mydb).query_db(query,data)
        return results
    
    @classmethod # METHOD TO EDIT AND UPDATE PIES
    def edit(cls,data):
        query = ''' UPDATE pies SET name = %(name)s, filling = %(filling)s, crust = %(crust)s WHERE id = %(id)s;'''
        results = connectToMySQL(mydb).query_db(query,data)
        return results
    
    @classmethod # METHOD TO DELETE THE PIES
    def delete(cls,data):
        query = ''' DELETE FROM pies WHERE id = %(id)s;'''
        results = connectToMySQL(mydb).query_db(query,data)
        return results
    
    @classmethod # METHOD TO SELECT BY ID FOR THE BAKER
    def get_by_id(cls,data):
        query = ''' SELECT * FROM pies WHERE baker_id = %(id)s;'''
        result = connectToMySQL(mydb).query_db(query,data)
        output = []
        print(result)
        for row in result:
            output.append(cls(row))
        return output
    
    @classmethod # METHOD TO SELECT BY ID WITH JOIN STATEMENT ########################################################################################################################################################
    def get_all(cls):
        query = '''SELECT * FROM pies JOIN users ON pies.baker_id = users.id ORDER BY votes DESC;'''
        results = connectToMySQL(mydb).query_db(query)
        return results
    
    @classmethod # METHOD WITH JOIN STATEMENT TO GET A SINGLE PIE WITH CORROBORATING BAKER AND USER ID
    def get_one(cls,data):
        query = '''
        SELECT * FROM pies JOIN users ON pies.baker_id = users.id WHERE pies.id = %(id)s;'''
        results = connectToMySQL(mydb).query_db(query,data)[0]
        print(results)
        return results
    
    @staticmethod
    def validate_pie(pie):
        is_valid = True
        if len(pie['name']) < 2:
            flash('Pie must have at least 2 characters in name.', 'add_pie')
            is_valid = False
        if len(pie['filling']) < 2:
            flash('Pie must have at least 2 characters in filling.', 'add_pie')
            is_valid = False
        if len(pie['crust']) < 2:
            is_valid = False
            flash('Pie must have at least 2 characters in crust', 'add_pie')
        return is_valid    @staticmethod
    def validate_pie(pie):
        is_valid = True
        if len(pie['name']) < 2:
            flash('Pie must have at least 2 characters in name.', 'add_pie')
            is_valid = False
        if len(pie['filling']) < 2:
            flash('Pie must have at least 2 characters in filling.', 'add_pie')
            is_valid = False
        if len(pie['crust']) < 2:
            is_valid = False
            flash('Pie must have at least 2 characters in crust', 'add_pie')
        return is_valid
    
    # @classmethod #dojoninja
    # def get_one_pie(cls, data):
    #     query = """
    #     SELECT * FROM users LEFT JOIN pies on pies.baker_id = users.id WHERE pies.id = %(id)s; """
    #     results = connectToMySQL(mydb).query_db(query, data)
    #     if not results:
    #         return []
    #     user = cls(results[0])
    #     for item in results:
    #         n = {
    #                 'id': item['pies.id'],
    #                 'name': item['name'],
    #                 'filling' : item['filling'],
    #                 'crust' : item['crust'],
    #                 'created_at' : item['created_at'],
    #                 'updated_at' : item['updated_at'],
    #                 'baker_id' : item['baker_id'],
    #                 'consumer_id' : item['consumer_id'],
    #             }
    #         user.pies.append(pie.Pie(pie_data))
    #         return user
"""
    #@classmethod
    #def get_oneNinja(cls, data):
        # Using a Left Join will enable us to return ninja assigned to dojo.id
          query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        if not results:
               return []
               # if this query comes back as a false value or empty list it prevents the run. put it in all of your class methods after the results so it doesn't continue breaking your code
        print(results)
        dojo = cls(results[0])
        for item in results:
            n = {
                    'id': item['ninjas.id'],
                    'first_name': item['first_name'],
                    'last_name' : item['last_name'],
                    'age' : item['age'],
                    'created_at' : item['created_at'],
                    'updated_at' : item['updated_at']
               }
               dojo.ninja.append(Ninja(n))
          return dojo
"""