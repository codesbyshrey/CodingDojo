# THIS IS OUR CHECKLIST PAGE FOR NOW IN USER CRUD MOD
# MAKE SURE TO COPY THIS PAGE ONCE FULLY ESTABLISHED
# THIS IS BOILERPLATE CODE, NO NEED TO RETYPE EVERY SINGLE TIME

# A cursor is the object we use to interact with the database
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

     # The METHOD to query the database
     # This allows us to use our SQL queries and interact with the database
     
     def query_db(self, query, data=None):
          with self.connection.cursor() as cursor:
               try:
                    query = cursor.mogrify(query, data)
                    print("Running the Query:", query)

                    cursor.execute(query)
                    if query.lower().find("insert") >= 0:
                         # INSERT queries will return an ID NUM corresponding to row
                         self.connection.commit()
                         return cursor.lastrowid
                    elif query.lower().find("select") >= 0:
                         # SELECT queries will return database data as a LIST OF DICTS
                         result = cursor.fetchall()
                         return result
                    else:
                         #UPDATE and DELETE queries return nothing
                         self.connection.commit()
               except Exception as e:
                    # If the query fails, the method should reutrn False (bool)
                    print("Something went wrong", e)
                    return False
               finally:
                    # Close the connection
                    self.connection.close()

#connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
# This is a very important step

def connectToMySQL(db):
     return MySQLConnection(db)
