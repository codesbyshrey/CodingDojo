from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the name table from our database
DB = "dojos_and_ninjas_schemea"

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    # Now we use class methods to query our database
    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"
        user_id = connectToMySQL(DB).query_db(query, data)
        return user_id
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DB).query_db(query)
        all_ninjas = []

        for dict in results:
            all_ninjas.append( cls(dict) )
        return all_ninjas
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"
        result = connectToMySQL(DB).query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_one(cls, data):
        query = """UPDATE ninjas 
        SET first_name = %(first_name)s,
        last_name = %(last_name)s,
        age = %(age)s
        WHERE id = %(id)s;
        """
        result = connectToMySQL(DB).query_db(query, data)
        return result

    @classmethod
    def delete_one(cls, data):
        query = """DELETE FROM ninjas
        WHERE id = %(id)s;
        """
        result = connectToMySQL(DB).query_db(query, data)
        return result