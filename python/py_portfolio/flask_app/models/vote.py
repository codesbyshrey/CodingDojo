from sqlite3 import DatabaseError
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

from flask import flash, session

DATABASE = "voting_db"

class Vote:
    def __init__(self, data):
        self.id = data['id']
        self.user_vote_id = data['user_vote_id']
        self.pie_id = data['pie_id']
        if 'created_at' in data:
            self.created_at = data['created_at']
        if 'updated_at' in data:
            self.updated_at = data['updated_at']

#======================= Check if user voted recipe ==============
    @classmethod
    def user_vote(cls, data):
        
        query = "SELECT * FROM votes WHERE user_vote_id = %(voter_id)s && pie_id = %(pie_id)s"

        result = connectToMySQL(DATABASE).query_db(query, data)

        vote = []
        for items in result:
            vote.append(cls(items))
        
        if len(vote) > 0:
            return 1
        else:
            return 0


#========================== Create Vote =====================
    @classmethod
    def create_vote(cls,data):

        query = "INSERT INTO votes (user_vote_id, pie_id, created_at, updated_at) VALUES (%(voter_id)s, %(pie_id)s, NOW(), NOW());"

        connectToMySQL(DATABASE).query_db(query, data)

        return

#========================== Delete Vote =====================
    @classmethod
    def delete_vote(cls,data):

        query = "DELETE FROM votes WHERE user_vote_id = %(voter_id)s && pie_id = %(pie_id)s;"

        connectToMySQL(DATABASE).query_db(query, data)

        return