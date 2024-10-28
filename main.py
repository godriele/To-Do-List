from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.secret_key = "To-Do-List"

# I configured SQL Alchemy to work with flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACL_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#TODO: Create a Database Model
# Every user will have their own model, unique ID for each user, username and password
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), unique=True, nullable=False)
    # People can only create a username with onyl 12 characters
    # People cant leave the usernmae and password blank
    password= db.Column(db.String(12), nullabale=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        # In here so whatever the users put in for their password, 
        # the module generate_has will turn it into hash for protection
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        # if the password the user put is wrong then it will return False, otherwise True
