from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.secret_key = "To-Do-List"

# Todo: I configured SQL Alchemy to work with flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACL_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Todo: Create the Database Model
# Every user will have their own model, unique ID for each user, username and password
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), unique=True, nullable=False)
    # People can only create a username with onyl 12 characters
    # People cant leave the usernmae and password blank
    password= db.Column(db.String(12), nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        # In here so whatever the users put in for their password, 
        # the module generate_has will turn it into hash for protection
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        # if the password the user put is wrong then it will return False, otherwise True

# Todo: Create the neccessary routes I need (Home, Login, Register, Dashboarrd, Logout)

# * Home Route
@app.route('/')
def home():
    if "username" in session:
        return redirect(url_for('dashbaord'))
    return render_template('index.html')

# * Login Route

@app.route('/login', method=['POST'])
def login():
    
    username = request.form.get("username")
    password = request.form.get("password")
    # Using .get() to avoid KeyError
    
    # Im using a raw SQL query to get the password for the given usernmae
    user_password = db.session.execute(
        text("SELECT password_hash FROM user WHERE username = :username"), # use text() here
        {"username": username}
    ).scalar() # .scalar() will get first result or none
    
    # To check if the user password exists and verify it
    if user_password and check_password_hash(user_password, password):
        session["username"] = username  # This will store the username in session
        return redirect(url_for('dashboard')) # if the users is in, this will redirect them to the dashboard
    else:
        return render_template("index.html", error="Wrong information") # Will show error if users put in the wrong info 

# * Register Route



# * Dashboard Route
# * Logout Route

#Todo: Create Database
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    # This will create our instance folder with users.db inside of it