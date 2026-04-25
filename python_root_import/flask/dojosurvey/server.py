from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def info ():
     return render_template('index.html')

@app.route ('/process_form', methods=['POST'])
def process_form():
     session['name'] = request.form['name']
     session['location'] = request.form['location']
     session['fav_lang'] = request.form['fav_lang']
     session['comment'] = request.form['comment']
     print(session)
     return redirect('/formresult')

@app.route('/formresult')
def result_form():
     return render_template('result.html')

if __name__ =="__main__":
     app.run(debug=True)
     #app.run(port=5000)

# i need the app.run line on Mac for some reason, not for windows / it always launches at port=5000
# I wonder how live server constantly launches at port 5500 as well, what's the code behind that functionality