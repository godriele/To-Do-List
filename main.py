from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.secret_key = "To-Do-List"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACL_MODIFICATIONS"] = False
db = SQLAlchemy(app)