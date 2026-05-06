from flask import Flask, render_template, redirect, session 
# dont forget to import redirect
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def show_user():
     if "one" not in session:
          session["one"] = 1
     else: 
          session["one"] += 1
     return render_template('index.html')

@app.route('/destroy_session')
def no_show():
     session.clear()
     return redirect("/")

@app.route("/add_more")
def show_more():
     if "one" not in session:
          session["one"] = 1
     else: 
          session["one"] += 1
     return redirect('/')

if __name__=="__main__":
     app.run(debug=True)
     # app.run(port=5000)