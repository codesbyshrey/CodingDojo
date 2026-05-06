# Howdy to new server, make your new stuff
# something about windows doesn't like installing flask anymore, we'll have to go and sort that out but at least we got it to work again on the Mac
# occasionally gives me an error that it can't find flask?? tf 
# pipfile and pipfile.lock always have to be available

# NINJA BONUS - try and do it all within a single template

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def initial():
     return "Welcome to Playground Application"

@app.route('/play')
def play():
     return render_template('index.html')

# I WILL NEVER USE ANGLE BRACKETS EXCEPT IN THE ROUTE

@app.route('/play/<int:number_box>')
def play_box(number_box):
     return render_template('idx2.html', repeat = number_box)

@app.route('/play/<int:number_box>/<string:color>')
def box_color(number_box, color):
     return render_template('idx3.html', repeat = number_box, color=color)

# THIS ALWAYS GOES AT THE BOTTOM
if __name__ == "__main__":
     app.run(debug=True)
