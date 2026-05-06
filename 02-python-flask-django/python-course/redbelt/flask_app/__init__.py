from flask import Flask
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

#app secret key HAS to be included to permit session to store cookies securely