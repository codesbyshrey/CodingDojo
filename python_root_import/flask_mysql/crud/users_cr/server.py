from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)

# more or less the same format as dojo survey

@app.route('/')
def read_all():
     return redirect('/users')

@app.route('/users')
def users_all():
     return render_template("users.html", users=User.get_all())

@app.route('/user/new')
def user_new():
     return render_template("new_user.html")

@app.route('/user/create', methods=['POST'])
def user_create():
     print(request.form)
     User.save(request.form)
     return redirect ('/users')

if __name__ == "__main__":
     app.run(debug=True)