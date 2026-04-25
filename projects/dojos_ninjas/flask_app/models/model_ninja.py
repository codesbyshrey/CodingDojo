from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    DB = "dojos-and-ninjas-schema"

    def __init__(self, data):
        self.id = data["id"]
        self.dojo_id = data["dojo_id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUES (%(dojo)s, %(fname)s, %(lname)s, %(age)s, NOW(), NOW())"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result[0]

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        for entry in results:
            ninjas.append(cls(entry))
        return ninjas

    @classmethod
    def update_one(cls, data):
        query = "UPDATE ninjas SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s, updated_at=%(time)s WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result