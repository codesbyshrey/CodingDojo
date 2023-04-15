# Mac and Windows alternating with their Flask issues how lovely
# submit this as long as it works then uninstall everywhere / globally and reinstall

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def names():
     users = [
          {'first_name' : 'Michael', 'last_name' : 'Choi'},
          {'first_name' : 'John', 'last_name' : 'Supsupin'},
          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
          {'first_name' : 'KB', 'last_name' : 'Tonel'},
          {'first_name' : 'Shreyas', 'last_name' : 'Sriram'}
     ]
     return render_template('index.html', user = users)

if __name__ =="__main__":
     app.run(debug=True)