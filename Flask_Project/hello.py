from flask import Flask, flash , render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone






# craete a flask instance 
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Hariom%402004@localhost:3306/users"
app.config['SECRET_KEY'] = '1234'
db = SQLAlchemy(app)  # create a database instance and intialize the database with the app instance
# create a model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    def __repr__(self):
        return f'<User {self.name}>'
    
class UserForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your email?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        user =User.query.filter_by(email=email).first()
        if user is None:
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            name =form.name.data
            form.name.data = ''
            form.email.data = ''
        flash('User created successfully')
    our_users = User.query.order_by(User.date_created)
    return render_template('add_user.html', form=form, name=name,our_users=our_users)














if __name__ == '__main__':
    app.run(debug=True) # it will run the server on localhost:5000 and dyanamicly update the server when you change the code
    # app.run() # it will run the server on localhost:5000

# define a route
@app.route('/')
def index():
    #return "Hello bhhhj world" # you can write a html tage  code here , it will works 
    flash('welcome to our website ')
    return render_template('index.html')





@app.route('/user/<name>')
def user(name):
    #return f'Hello {name}'
    # you can set variables in html file and pass the value from here
    favourite_food = ['Pizza', 'Burger', 'Pasta']
    return render_template('user.html', user_name=name, favourite_food=favourite_food)
# you can set in terminal export FLASK_APP=hello.py || no space in this  && export FLASK_ENV=development

# jinja is a templating library for python, it is used to create html templates in flask


#  create error handler in flask
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# internel server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# create a form  class in flask
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

# create a route for name form
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash('Form submitted successfully')
    return render_template('name.html', form=form, name=name)




# list of others wtf fields and validators
# BooleanField : Represents an HTML <input type="checkbox">.
# DateField : Represents an HTML <input type="date">.
# DateTimeField : Represents an HTML <input type="datetime-local">.
# DecimalField : Represents an HTML <input type="number"> with a step attribute of 0.01.
# FileField : Represents an HTML <input type="file">.
# HiddenField : Represents an HTML <input type="hidden">.
# MultipleFileField : Like FileField, but allows multiple files to be uploaded.
# PasswordField : Represents an HTML <input type="password">.
# RadioField : Represents an HTML <input type="radio">.
# SelectField : Represents an HTML <select> element.
# SelectMultipleField : Like SelectField, but allows multiple options to be selected.
# SubmitField : Represents an HTML <input type="submit">.
# TextAreaField : Represents an HTML <textarea> element.
# URLField : Represents an HTML <input type="url">.


# list of validators
# DataRequired : Makes the field required.
# Email : Validates an email address.
# EqualTo : Compares the values of two fields; useful for password confirmation.
# IPAddress : Validates an IPv4 network address.
# Length : Validates the length of the field’s data.    
# NumberRange : Validates that the field’s data is within a numeric range.
# Optional : Allows the field to be empty.
# Regexp : Validates the field’s data against a regular expression.


# explain include and extends in jinja
# include : include is used to include the content of one template into another template.
# extends : extends is used to inherit the content of one template into another template. The child template can override the blocks defined in the parent template.


# passing parameters to url
# url_for('user', name='John Doe')


# give me code to add the css  file from the static folder 
# <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">  # here style.css is the file name in the static folder


