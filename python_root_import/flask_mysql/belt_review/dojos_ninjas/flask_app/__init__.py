from flask import Flask
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

# Secret Key is a method to help keep cookie safe
# Can be anything, we are just used to using this