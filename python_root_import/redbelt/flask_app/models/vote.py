# the most realistic way to implement the votes will be to create a third table in my workbench --> thinking of it in javascript is way to freaking weird and silly to try and keep referencing right now. idk how to do many-to-many

# one to many from pies to users --> user_pie_id KEEP IT SINGULAR STUPID
# one to many from votes to users --> user_vote_id KEEP IT SINGULAR STUPID 
# one to many from votes to pies --> pie_id KEEP IT SINGULAR STUPID
# DON'T FORGET TO REVERSE ENGINEER BEFORE YOU MAKE THE CHANGES
# DON'T FORGET TO FORWARD ENGINEER AGAIN AFTER ADDING THE TABLE

from flask_app.config.mysqlconnection import connectToMySQL

DB = "pie_derby" # this lets me just throw in DB anytime I need the connectToMySQL so I stop confusing myself in silly ways

class Vote:
     def __init__(self, data):
          self.id = data['id']
          self.user_vote_id = data['user_vote_id']
          self.pie_id = data['pie_id']
          self.created_at = data['created_at']
          self.updated_at = data['updated_at']
     # CLASS CREATION OF VOTES IS NOW COMPLETE

### CLASS METHODS PROVIDED BELOW

# Class method to add a vote
@classmethod
def add_vote(cls, data):
     query = "INSERT INTO votes (user_vote_id, pie_id) VALUES (%(voter_id)s, %(pie_id)s);"
     results = connectToMySQL(DB).query_db(cls, data)
     return results

# Class method to Delete a Vote
# bruh SQL countries is mad clutch for this assignment thank god i did it
@classmethod
def del_vote(cls, data):
     query = "DELETE FROM votes WHERE user_vote_id = %(voter_id)s && pie_id = %(pie_id)s;"
     results = connectToMySQL(DB).query_db(cls, data)
     return results


# LATER ON - CLASS METHOD TO SEE IF THE LOGGED IN USER IS TRYING TO VOTE AGAIN FOR THEMSELVES
# probably just same as delete function but select from instead, and then some kind of if statement to establish if the user has already added a vote, with else statement to allow a vote to go through