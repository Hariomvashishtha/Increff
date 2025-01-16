# how to create the virtual environment   python3 -m venv .venv
# how to activate the virtual environment  source .venv/bin/activate
# how to deactivate the virtual environment  deactivate
# how to install flask  pip install flask
# how to run the flask app  python app.py
# how to install flask_sqlalchemy  pip install flask_sqlalchemy


# How to create a database in flask
# 1. Import the necessary modules
# 2. Create an instance of the Flask class
# 3. Set the configuration key
# 4. Create an instance of the SQLAlchemy class
# 5. Create the database
# 6. Create the tables
# 7. Commit the changes
# 8. Close the connection


# How to create a table in flask
# 1. Create a class that inherits from the db.Model class
# 2. Define the columns of the table
# 3. Define the relationships between tables
# 4. Define the constraints of the table
# 5. Define the methods of the table
# 6. Define the properties of the table


# basic flask app 
from flask import Flask, flash, redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

# ho to run the flask app   python app.py   flask --app hello run
# how to run the flask app in debug mode  python app.py  flask --app hello run --debugger

# html escaping 
from markupsafe import escape
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


# variable  rules in the path 
@app.route("/<int:id>")
def get_user(id):
    return f"User {id}"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/uuid/<uuid:uuid>')
def show_uuid(uuid):    
    return f'UUID {uuid}

# how to redirect the user to another page
from flask import redirect, url_for
@app.route('/login') 
def login():
    return redirect(url_for('index'))


# use of the trainling slash  both the routes differ in their use due to the presence and absence of the trailing slash
@app.route('/projects/')
def projects():
    return 'The project page'
@app.route('/about')
def about():
    return 'The about page'

# how to build the urls 
from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
# /
# /login
# /login?next=/
# /user/John%20Doe


# multiple routes for the same view function , we are writing the same view function for the two routes
from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login() # type: ignore
    else:
        return show_the_login_form() # type: ignore

# url for the static files 
url_for('static', filename='style.css')  # when you want to generate the url for the static files like css

# how to render the template in the flask ,2 routes are defined for the same view function
from flask import render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

# <!doctype html>
# <title>Hello from Flask</title>
# {% if person %}
#   <h1>Hello {{ person }}!</h1>
# {% else %}
#   <h1>Hello, World!</h1>
# {% endif %}

# access the request object
from flask import request
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return do_the_login() # type: ignore
    else:
        return show_the_login_form() # type: ignore
    
from flask import request

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'


# how to handle the file upload in the flask
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')

# how to access the cookies in the flask
from flask import request
@app.route('/')
def index():
    username = request.cookies.get('username')

from flask import make_response

# how to set the cookies in the flask
@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

# how to handle the error in the flask
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# session , this is basically used to maintain and store the state between the clent and the server , store user specific 
# information on the server while user is log in or interacting with the server like tokens,cart items etc

from flask import session

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# how to basically made a db connection in the flask
# here g is the special function that is used to store the data that is shared between the request and the response
# same connectionc can be used if the getdb() is called multiple times in the same request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from datetime import datetime
import click
from flask import current_app, g
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# how to craete tables in the flask
# this will be in the schema.sql file , after that write code to run this sql 
# DROP TABLE IF EXISTS user;
# DROP TABLE IF EXISTS post;

# CREATE TABLE user (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   username TEXT UNIQUE NOT NULL,
#   password TEXT NOT NULL
# );

# CREATE TABLE post (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   author_id INTEGER NOT NULL,
#   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   title TEXT NOT NULL,
#   body TEXT NOT NULL,
#   FOREIGN KEY (author_id) REFERENCES user (id)
# );

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)



# blueprints in the flask
# is used to org the group of the reloadted views and the other code

# i am writing code for the register the user in the  and applying auth and storing in the table 
bp.route('/register', methods=('GET', 'POST')) # type: ignore
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)), # type: ignore
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


# to logout the error  , remove the id from the session
@bp.route('/logout') # type: ignore
def logout():
    session.clear()
    return redirect(url_for('index'))


# basic templates for the flask
# <!doctype html>
# <title>{% block title %}{% endblock %} - Flaskr</title>
# <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
# <nav>
#   <h1>Flaskr</h1>
#   <ul>
#     {% if g.user %}
#       <li><span>{{ g.user['username'] }}</span>
#       <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
#     {% else %}
#       <li><a href="{{ url_for('auth.register') }}">Register</a>
#       <li><a href="{{ url_for('auth.login') }}">Log In</a>
#     {% endif %}
#   </ul>
# </nav>
# <section class="content">
#   <header>
#     {% block header %}{% endblock %}
#   </header>
#   {% for message in get_flashed_messages() %}
#     <div class="flash">{{ message }}</div>
#   {% endfor %}
#   {% block content %}{% endblock %}
# </section>



# {% extends 'base.html' %}
# {% block header %}
#   <h1>{% block title %}Register{% endblock %}</h1>
# {% endblock %}
# {% block content %}
#   <form method="post">
#     <label for="username">Username</label>
#     <input name="username" id="username" required>
#     <label for="password">Password</label>
#     <input type="password" name="password" id="password" required>
#     <input type="submit" value="Register">
#   </form>
# {% endblock %}


# executing the delete query in the api of the flask 
@bp.route('/<int:id>/delete', methods=('POST',)) # type: ignore
@login_required # type: ignore
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))

# Within an application context, get_db should return the same connection each time it’s called. After the context, the connection should be closed.
# how to create the connection with the db, this is basically get_db() function that is used to create the connection with the db

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

# autoescaping the special chars in the html in the flask 
# {% autoescape false %}
#     <p>autoescaping is disabled here
#     <p>{{ will_not_be_escaped }}
# {% endautoescape %}

# how to use the filters in the flask
# this is for reversing the object 
@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

def reverse_filter(s):
    return s[::-1]
app.jinja_env.filters['reverse'] = reverse_filter


# fixtures helps me to write a code that can be reuseble across the test cases

# accessing and the modify the session of the flask 
# To access Flask’s context variables, mainly session, use the client in a with statement. The app and request context will remain active after making a request, until the with block ends.
from flask import session
def test_access_session(client):
    with client:
        client.post("/auth/login", data={"username": "flask"})
        # session is still accessible
        assert session["user_id"] == 1
    # session is no longer accessible

# how to implement the 404 error in the flask, we are defining this in our own way 
from flask import render_template
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


# how to do logging in the flask , we have to use app.logger for logging in the  flask 
@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])

    if user.check_password(request.form['password']):
        login_user(user) # type: ignore
        app.logger.info('%s logged in successfully', user.username)
        return redirect(url_for('index'))
    else:
        app.logger.info('%s failed to log in', user.username)
        abort(401)



# configurato basics in the flask 
app = Flask(__name__)
app.config['TESTING'] = True
app.testing = True
app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

# signals in the flask
# thses are lightweight way to notify the subscribers that some action has taken place in the application
# this is implemented using the blinker library

# this is basic reuseable view 
@app.route("/users/")
def user_list():
    users = User.query.all()
    return render_template("users.html", users=users)

# all details about the application context in the flask
#  Application context is created before the request comes in and is destroyed as soon as the request finishes.

# extension in the flask 
# flask  is basically made a very lightweight and extensible framework and these allow developers to add the functionality to the flask such auth, db connection and the intregation 


# command line interface in the flask

# in flast you can easily make the database connection on the demansd and close the connection after the work is done
import sqlite3
from flask import g
DATABASE = '/path/to/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
# how to connect the db on the demand 
with app.app_context():
    db = get_db()
    # do something with the database
    db.execute('CREATE TABLE ...')

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# how to  make the  connection with the db in the flask usin the 
# this is how we have to do the connection with the db in the flask using the sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine('sqlite:////tmp/test.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import yourapplication.models # type: ignore
    Base.metadata.create_all(bind=engine)

# creating the table from the model in the flask
from sqlalchemy import Column, Integer, String
from yourapplication.database import Base # type: ignore

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'
    
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from yourapplication.database import metadata, db_session # type: ignore

class User(object):
    query = db_session.query_property()

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), unique=True),
    Column('email', String(120), unique=True)
)
mapper(User, users)

# how to upload the files in the specific folder in the flask
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# now we are going to learn the decorators in the flask
# this is basically used to modify the function or the method in the python
# A decorator is a function that wraps and replaces another function. Since the original function is replaced, you need to remember to copy the original function’s information to the new function. Use functools.wraps() to handle this for you.
@app.route('/')
def index():
    return render_template('index.html', value=42)

@app.route('/')
@templated('index.html') # type: ignore
def index():
    return dict(value=42)

@app.route('/')
@templated() # type: ignore
def index():
    return dict(value=42)

# how to use validators in the flask
from wtforms import Form, BooleanField, StringField, PasswordField, validators # type: ignore

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


# Flashing system , flask  has this to show or give feedback to the user, so that they will love the application
from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

# we can also filter the messages in the flash like error catogry msg i want to filter 
# This is layout.html which is basically doing the magic 
# <!doctype html>
# <title>My Application</title>
# {% with messages = get_flashed_messages() %}
#   {% if messages %}
#     <ul class=flashes>
#     {% for message in messages %}
#       <li>{{ message }}</li>
#     {% endfor %}
#     </ul>
#   {% endif %}
# {% endwith %}
# {% block body %}{% endblock %}

# how to make connection with the mongodb 
from flask import Flask
from flask_mongoengine import MongoEngine 

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": "myapp",
}
db = MongoEngine(app)

# create a document in the mongodb
class Movie(me.Document):
    title = me.StringField(required=True)
    year = me.IntField()
    rated = me.StringField()
    director = me.StringField()
    actors = me.ListField()
# frozen set is immutabale form of the set in which no read or write operation can be performed.but this makes them hashable
# and can be used as the key in the dictionary




def hello_world():
   return "hello world"
app.add_url_rule("/", "hello", hello_world)
# this add_url_rule is used to  bind the url in the function 


# this is for the jinja template in the flask
# {% ... %} for Statements
# {{ ... }} for Expressions to print to the template output
# {# ... #} for Comments not included in the template output
# # ... ## for Line Statements


# Flask.abort(code)
# this is used to raise the error in the flask 

# {% with messages = get_flashed_messages() %}
#    {% if messages %}
#       {% for message in messages %}
#          {{ message }}
#       {% endfor %}
#    {% endif %}
# {% endwith %}
# this is for the flash message in the flask 