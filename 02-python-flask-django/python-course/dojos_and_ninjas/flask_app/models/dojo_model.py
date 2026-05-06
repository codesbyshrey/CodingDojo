from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model
# model the class after the name table from our database
DB = "dojos_and_ninjas_schemea"

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    # Now we use class methods to query our database
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUE (%(name)s)"
        user_id = connectToMySQL(DB).query_db(query, data)
        return user_id
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DB).query_db(query)
        all_dojos = []

        for dict in results:
            all_dojos.append( cls(dict) )
        return all_dojos

    @classmethod
    def get_one_with_many(cls, data):
        query = """
        SELECT * FROM dojos LEFT JOIN ninjas on ninjas.dojo_id =
        dojos.id WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(DB).query_db(query, data)
        dojo = cls(results[0])

        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"],
                "dojo_id" : row_from_db["dojo_id"]
            }
            dojo.ninjas.append( ninja_model.Ninja(ninja_data))
        return dojo
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        result = connectToMySQL(DB).query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_one(cls, data):
        query = """UPDATE dojos 
        SET name = %(name)s
        WHERE id = %(id)s;
        """
        result = connectToMySQL(DB).query_db(query, data)
        return result

    @classmethod
    def delete_one(cls, data):
        query = """DELETE FROM dojos
        WHERE id = %(id)s;
        """
        result = connectToMySQL(DB).query_db(query, data)
        return result