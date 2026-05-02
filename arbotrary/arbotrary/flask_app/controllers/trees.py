from flask_app import app
from flask import flash, render_template, request, redirect, session
from flask_app.models.recipe import Recipe

# DON'T EVEN BOTHER RENAMING RIGHT NOW, IT'S FUNCTIONAL
# FOR SOME REASON RENAMING EVEN WITHIN THE CONTROLLERS FUNCTIONS DIDN'T LEAD TO ERRORS BUT JUST REFUSED TO ADD THEM TO MY DASHBOARD PAGE, I DON'T WANT TO DEAL WITH SUCH ISSUES. WE CAN ADDRESS THEM AFTER WE GET OUR FIFTH TEMPLATE PAGE GOING

# @app.route('/view')
# def view_tree():
#     if 'email' not in session:
#         return redirect('/')
#     data = {
#         "id" : id
#     }
#     current_tree = Recipe.get_one_with_user(data)
#     return render_template( "view.html", current_tree=current_tree)

# ---------------------------------------------- DISPLAYING RECIPES ON DASHBOARD
@app.route( '/recipes')
def display_recipes():
    if 'email' not in session:
        return redirect( '/' )
    list_recipes = Recipe.get_all_with_users()
    return render_template( 'recipes.html', list_recipes = list_recipes )

# effectively just the same as up above
@app.route( '/usertrees' )
def display_user_tree():
    if 'email' not in session:
        return redirect( '/' )
    user_recipes = Recipe.get_all_with_users()
    return render_template( "usertrees.html", user_recipes = user_recipes)

@app.route( '/recipe/new' )
def display_create_recipe():
    if 'email' not in session:
        return redirect( '/' )
    return render_template( "create_recipe.html" )

#----------------------------------------------------------- CREATING RECIPE
@app.route( '/recipe/create', methods = ['POST'] )
def create_recipe():
    if Recipe.validate_recipe( request.form ) == False:
        return redirect( '/recipe/new' )

    data = {
        **request.form,
        "user_id" : session['user_id']
    }

    Recipe.create( data )
    return redirect( '/recipes' )

# ---------------------------------------------------------- DISPLAYING RECIPES
# NEED TO ADD A DISPLAY USER RECIPE SPECIFICALLY FOR WIREFRAME 4
@app.route( '/recipes/<int:id>' )
def display_one( id ):
    if 'email' not in session:
        return redirect( '/' )
    data = {
        "id" : id
    }
    current_recipe = Recipe.get_one_with_user( data )
    return render_template( "recipe.html", current_recipe = current_recipe )

### framework for wireframe 4 route is copied up from above but placed further above

@app.route( '/recipes/<int:id>/update' )
def display_update_recipe( id ):
    if 'email' not in session:
        return redirect( '/' )
    data = {
        "id" : id
    }
    current_recipe = Recipe.get_one_with_user( data )
    return render_template( "update_recipe.html", current_recipe = current_recipe )

# ------------------------------------------------------------ UPDATE AND DELETE
@app.route( '/recipe/update/<int:id>', methods = ['POST'] )
def update_recipe( id ):
    if Recipe.validate_recipe( request.form ) == False:
        return redirect( f'/recipes/{id}/update' )
    recipe_data = {
        **request.form,
        "id" : id
    }
    Recipe.update_one( recipe_data )
    return redirect( '/recipes' )

@app.route( '/recipes/<int:id>/delete' )
def delete_recipe( id ):
    data = {
        "id" : id
    }
    Recipe.delete_one( data )
    return redirect( '/recipes' )