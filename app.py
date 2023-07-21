from flask import Flask,Response,session, request, render_template,flash,redirect, url_for
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

MONGO_URI = "mongodb+srv://sajjad:Sajjad%40321@cluster0.xh2jqt2.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client.get_database("Test") 
collection =  db["user"]
app.secret_key = "test11"


@app.route('/')
def hello():
    if 'user' in session:
    # Use the user_id to fetch user data from the database if needed
        return redirect(url_for('admin'))
    else:
        return render_template('index.html')

    

@app.route('/about-us')
def about():
    if 'user' in session:
    # Use the user_id to fetch user data from the database if needed
        return redirect(url_for('admin'))
    else:
       return render_template('about-us.html')
   

@app.route('/contact-us')
def contact():
    if 'user' in session:
    # Use the user_id to fetch user data from the database if needed
        return redirect(url_for('admin'))
    else:
       return render_template('contact-us.html')
    

@app.route('/login',methods=['GET'])
def login_form():

    if 'user' in session:
    # Use the user_id to fetch user data from the database if needed
        return redirect(url_for('admin'))
    else:
       return render_template('login.html')
    
    


@app.route('/register')
def register_form():
    if 'user' in session:
    # Use the user_id to fetch user data from the database if needed
        return redirect(url_for('admin'))
    else:
       return render_template('register.html')
    

@app.route('/register',methods=['POST'])
def register():
     # Replace "<database>" with your database name

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    collection =  db["user"]

    user = collection.find_one({"email": email})

    if user: 
        flash('Email Already taken', 'error')
        return redirect(url_for('register'))
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        collection =  db["user"]
        data = {"name": name, 'email':email,'password':password}
        collection.insert_one(data)
        flash('Register Successfully', 'error')
        return redirect(url_for('login'))

@app.route('/login',methods=['POST'])
def login():

    email = request.form['email']
    password = request.form['password']
    user = collection.find_one({"email": email, "password": password})

    if user:
  
        session['user'] = str(user["_id"])
        session['name'] = str(user["name"])
        session['email'] = str(user["email"])
        flash('login Successfully', 'error')
        return redirect(url_for('admin'))
    else:
        flash('"Invalid email or password.', 'error')
        return redirect(url_for('register'))
    
@app.route('/admin',methods=['GET'])
def admin():

    if 'user' in session:
        # Use the user_id to fetch user data from the database if needed
       return render_template('admin-file.html')
      
    else:
        flash('login First to Access this Page', 'error')
        return redirect(url_for('login'))
   

@app.route('/logout')
def logout():
    if 'user' in session:
        # Use the user_id to fetch user data from the database if needed
       session.clear()
       flash('Logout Successfully', 'error')
       return redirect(url_for('login'))
    else:
        flash('Login First to Access this Page ', 'error')
        return redirect(url_for('login'))
   
app.run(debug=True)
