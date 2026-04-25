# Initialization file within flask_app that server needs to recognize

from flask import Flask

app = Flask(__name__)
app.secret_key = 'secretkeys'