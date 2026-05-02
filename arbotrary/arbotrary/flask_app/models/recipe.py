from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from flask_app.models.user import User

class Recipe:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.cooked_date = data['cooked_date']
        # took out the under-30 line here. going to try taking it out in the database after I've cleared it from the code. If it doesn't work then so be it we will keep it in for now
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create( cls, data ):
        query  = "INSERT INTO recipes( name, description, instructions, cooked_date, user_id ) VALUES( %(name)s, %(description)s, %(instructions)s, %(cooked_date)s, %(user_id)s );"
        return connectToMySQL( DATABASE ).query_db( query, data )

    @classmethod
    def get_all_with_users( cls ):
        query  = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL( DATABASE ).query_db( query )
        list_recipes = []
        for row in results:
            current_recipe = cls( row )
            user_data = {
                **row,
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at'],
                "id" : row['users.id']
            }
            current_user = User( user_data )
            current_recipe.user = current_user
            list_recipes.append( current_recipe )
        return list_recipes

    @classmethod
    def get_one_with_user( cls, data ):
        query  = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        result = connectToMySQL( DATABASE ).query_db( query, data )
        if len( result ) > 0:
            current_recipe = cls( result[0] )
            user_data = {
                **result[0],
                "created_at" : result[0]['users.created_at'],
                "updated_at" : result[0]['users.updated_at'],
                "id" : result[0]['users.id']
            }
            current_recipe.user = User( user_data )
            return current_recipe
        else:
            return None

    @classmethod
    def update_one( cls, data ):
        query  = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, cooked_date = %(cooked_date)s WHERE id = %(id)s;"
        return connectToMySQL( DATABASE ).query_db( query, data )

    @classmethod
    def delete_one( cls, data ):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL( DATABASE ).query_db( query, data )

    @staticmethod
    def validate_recipe( data ):
        is_valid = True
        if data['name'] == "":
            flash( "Species cannot be empty", "error_recipe_name" )
            is_valid = False
        if data['description'] == "":
            flash( "Location cannot be empty", "error_recipe_description" )
            is_valid = False
        if data['instructions'] == "":
            flash( "Reasons cannot be empty", "error_recipe_instructions" )
            is_valid = False
        if data['cooked_date'] == "":
            flash( "Must Choose a Date of Planting", "error_recipe_cooked_date" )
            is_valid = False
        if len( data['name'] ) < 3:
            flash( "Species should be at least 3 characters long", "error_recipe_name" )
            is_valid = False
        if len( data['description'] ) < 3:
            flash( "Location should be at least 3 characters long", "error_recipe_description" )
            is_valid = False
        if len( data['instructions'] ) < 3:
            flash( "Reasons should be at least 3 characters long", "error_recipe_instructions" )
            is_valid = False

        return is_valid