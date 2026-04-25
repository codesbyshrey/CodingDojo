#import the function that will return an instance of a connection
from restaurants.config.mysqlconnection import connectToMySQL
#model the class after the friend table from our database

DATABASE = 'rest_burg_db'

class Restaurant:
     def __init__(self, data_):
          self.id = data['id']
          self.created_at = data['created_at']
          self.updated_at = data['updated_at']

     # NOTE: add additional attributes

#CRUD // Create and INSERT INTO
     @classmethod

#Read - SELECTS || Now we use class methods to query our database

#Update - UPDATE

#Delete - DELETE