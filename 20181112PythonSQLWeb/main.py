from flask import *
from flask_login import login_required, login_url, login_user, LoginManager, UserMixin, logout_user, current_user, AnonymousUserMixin
from sqlite3 import *

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
  def __init__(self,id, username = None, email = None):
    self.id = id
    self.username = username
    self.email = email

def loadEmail(user_id):
    db = connect('WebAppDB')
    cursor = db.cursor()
    cursor.execute("SELECT email FROM Users WHERE id='" + user_id + "';")
    email = cursor.fetchone()[0]
    return email

def loadUsername(user_id):
    db = connect('WebAppDB')
    cursor = db.cursor()
    cursor.execute("SELECT username FROM Users WHERE id='" + user_id + "';")
    username = cursor.fetchone()[0]
    return username

def loadPassword(user_id):
    db = connect('WebAppDB')
    cursor = db.cursor()
    cursor.execute("SELECT password FROM Users WHERE id='" + user_id + "';")
    password = cursor.fetchone()[0]
    return password

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        db = connect('WebAppDB')
        cursor = db.cursor()
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM Users WHERE username='" + username + "' AND password='" + password + "';")
        data = cursor.fetchall()
        if len(data) == 0:
            print('[E] Incorrect credentials were inserted')
            return render_template('incorrect.html')
        else:
            cursor.execute("SELECT id FROM Users WHERE username ='" + username + "' AND password = '" + password + "';")
            user_id = cursor.fetchone()[0]
            session['user_id'] = user_id

            cursor.execute("SELECT username FROM Users WHERE username ='" + username + "' AND password = '" + password + "';")
            name = cursor.fetchone()[0]
            session['username'] = name

            cursor.execute("SELECT email FROM Users WHERE username ='" + username + "' AND password = '" + password + "';")
            email = cursor.fetchone()[0]
            session['email'] = email

            login_user(User(user_id, username = name, email = email))
            print('[S] User with name: ' + name + ' was succesfully logged on')
            return redirect("dashboard/", code=302)
    return render_template('login.html')

@app.route('/signup/', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        db = connect('WebAppDB')
        cursor = db.cursor()
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        cursor.execute('INSERT OR IGNORE INTO Users (username, email, password) VALUES ("' + username + '","' + email + '","' + password + '");')
        db.commit()
        if cursor.lastrowid == 0:
            print("[E] User with name: " + username + " was not inserted due to duplicate data")
            return render_template('duplicate.html')
        else:
            print("[S] User with name: " + username + " was succesfully inserted")
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    print('[S] ' + session['username'] + ' has logged out')
    return redirect(url_for('home'))

@app.route('/dashboard/')
@login_required
def protected():
    db = connect('WebAppDB')
    cursor = db.cursor()
    user_id = session['user_id']
    cursor.execute("SELECT FirstLogin FROM Users WHERE ID ='" + user_id + "';")
    firstLogin = cursor.fetchone()[0]
    if firstLogin == 1:
        return redirect(url_for('firstLogin'))
    else:
        load_user(user_id)
        print('[S] ' + session['username'] + ' has connnected to his dashboard')
        return render_template('you.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/firstLogin', methods=['GET','POST'])
@login_required
def firstLogin():
    db = connect('WebAppDB')
    cursor = db.cursor()
    user_id = session['user_id']
    cursor.execute("SELECT FirstLogin FROM Users WHERE ID ='" + user_id + "';")
    firstLogin = cursor.fetchone()[0]
    if firstLogin == 0:
        return redirect(url_for('home'))
    else:
        if request.method == 'POST':
            length = request.form['length']
            weight = request.form['weight']
            cursor.execute("INSERT INTO Usershealth (length, weight, userID) VALUES ('" + length + "','" + weight + "','" + user_id + "');")
            cursor.execute("UPDATE Users SET FirstLogin = 0 WHERE ID=" + user_id + ";")
            return render_template(url_for('home'))
        return render_template('firstlogin.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.config['SECRET_KEY'] = "The Secret Key"
    app.secret_key = "The Secret key"
    app.run(debug=1, host='0.0.0.0')