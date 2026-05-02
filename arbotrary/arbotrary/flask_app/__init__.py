from flask import Flask
import re

app = Flask( __name__ )
app.secret_key = "keep it secret keep it safe"

# inside your initialization function, you can keep these terms inside and have them declared at the entire app level - include them inside files just in case unless it causes some weird error due to overwriting

DATABASE = "arbotrary_db"
#makes it easier to only have to change a single line for a boilerplate file

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#easy REGEX implementation immediately across users