from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about-us')
def about():
    return render_template('about-us.html')

@app.route('/contact-us')
def contact():
    return render_template('contact-us.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')