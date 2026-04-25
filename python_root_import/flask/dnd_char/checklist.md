# pre-req
~This only needs to be done once on your computer
```
pip install pipenv
```

# Checklist
 ~ Steps We Need to Take to Go From Zero to Hello World
  - Create a folder in current assignment
  - Open terminal window, and create virtual environment with correct dependences
```
pipenv install flast
```
 - MAKE SURE WE HAVE PIPFILE AND PIPFILE.LOCK
 - JUMP into the virtual environment
 ```
 pipenv shell
 ```
 - File Structure
     - Project Folder
          - templates
               - index.html
          - static
               - style.css
               - script.js
          - pipfile
          - pipfile.loc
          - server.py: 
```py
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

# THIS WILL MOVE LOCATIONS LATER
# You want to make routes that are repeatable
# Simple Structure to Understand - Name routes same as function

@app.route('/')
def index():
     return render_template('index.html')

# END OF MOVING


# ALWAYS AT BOTTOM
if __name__ == "__main__":
     app.run(debug=True)
```