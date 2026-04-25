# a cursor is the object we use to interact with the database
import pymysql.cursors

# The First Class provides us an instance of a connection to a database

class MySQLConnection:
     def __init__ (self, db):
          #Establishes a username and password 
          conection = pymysql.connect(
               host = 'localhost',
               user = 'root',
               password = 'doubleroot',
               db = db,
               charset = 'utf8mb4',
               cursorclass = pymysql.cursors.DictCursor, autommit = True )
          #Establish a connection to the Database
          self.connection = connection