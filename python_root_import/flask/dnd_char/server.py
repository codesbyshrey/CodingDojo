from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

# THIS WILL MOVE LOCATIONS LATER

# Display Route
@app.route('/')
def index():
     if 'characters' not in session:
          # print("Building a New Fake Database")
          session['characters'] = []
          # Instantiating an empty list of characters
     return render_template('index.html')

# Action Route
@app.route('/process_character', methods=['POST'])
def process_character():
     print(request.form) # A Request Form is a Dictionary That Can't be Changed (Tuple)

     all_characters = session['characters']
     # print(f"All Characters: {all_characters}")

     data = {
          **request.form,
          # Extracts everything from request.form and puts it into a dictionary
          # This enables us to have a copy of the dictionary that we can edit
          'id' : len(all_characters)
     }

     all_characters.append(data)
     # print(f"All Characters: {all_characters}")

     session['characters'] = all_characters
     # ^ pulled from session, appended to it, and added back into session
     # There are likely better ways to do this
     # This will show up in your terminal || print("Doing Something")
     return redirect('/')

# Action Route (even though it's not post) so we REDIRECT
@app.route('/delete/<int:id>')
def delete_character(id):
     # Pull the Characters from session back into all characters
     # Pop the ID of the first one deleted based on the button
     # Reassign all characters back into session to overwrite
     all_characters = session['characters']
     all_characters.pop(id)
     session['characters'] = all_characters
     return redirect ('/')
# END OF MOVING


# ALWAYS AT BOTTOM
if __name__ == "__main__":
     app.run(debug=True)