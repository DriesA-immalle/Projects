from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welkom op deze pagina! Ga ook eens naar route hello!'

@app.route('/hello')
def hello():
    return 'Dit is de route Hello! Hello :)'

@app.route('/liltay')
def liltay():
    return 'Lil Tay out here flexing in the I8, I\'ve spent 100 thousand racks on this car'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'Welcome %s' % username