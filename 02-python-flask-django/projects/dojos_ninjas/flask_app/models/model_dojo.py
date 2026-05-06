from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_ninja import Ninja


class Dojo:
    DB = "dojos-and-ninjas-schema"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW())"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result[0]

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for entry in results:
            dojos.append(cls(entry))
        return dojos

    @classmethod
    def read_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE ninjas.dojo_id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        dojo = cls(results[0])
        for entry in results:
            ninja_data = {
                "id": entry["id"],
                "dojo_id": entry["dojo_id"],
                "first_name": entry["first_name"],
                "last_name": entry["last_name"],
                "age": entry["age"],
                "created_at": entry["created_at"],
                "updated_at": entry["updated_at"],
            }
            dojo.ninjas.append(ninja_data)
        return dojo

    @classmethod
    def update_one(cls, data):
        query = "UPDATE dojos SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s, updated_at=%(time)s WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result