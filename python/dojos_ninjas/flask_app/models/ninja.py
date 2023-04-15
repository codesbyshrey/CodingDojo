from flask_app.config.mysqlconnection import connectToMySQL

# Creating Class Ninja to match with the database we created
# Errors here could be because of improper relationship defining in our schema
# Verify about where / how the workbench and schema might need to be saved in terms of folder structure in case that's an error?
# Don't forget to forward engineer prior to enabling the connections

class Ninja:
     def __init__(self, data):
          self.id = data['id']
          self.first_name = data['first_name']
          self.last_name = data['last_name']
          self.age = data['age']
          self.created_at = data['created_at']
          self.updated_at = data['updated_at']

     @classmethod
     def save(cls, data):
          query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
          return connectToMySQL('dojos_ninjas').query_db(query, data)