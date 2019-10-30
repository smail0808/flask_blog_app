

call env/Scripts/activate

pip freeze > requirements.txt
# These dependencies can be installed using the pip install command:

pip install -r requirements.txt
```

## Basic App structure

#### Model structure

can be used for a simple app

```python
|Pfolder
|---|app.py  # all the python code here
|---|templates # html file
|   |---|index.html
|   |---|base.html
|---|static  # css, img and js file 
|   |---|css
|   |   |---|main.css
		
```

#### Package structure

```python
|Application
|---|__init__.py
|---|models.py
|---|forms.py
|---|views.py
|---|static
|   |---|css
|   |   |---|styles.css
|   |---|js
|   |   |---|app.js
|   |---|img
|---|templates
|   |---|index.html
|   |---|layout.hml
|run.py
```

####  Blueprint Structure

```python
|Application # the main package
|---|__init__.py
|---|config.py
|---|users # the sub package  
|   |---|__init__.py
|   |---|forms.py
|   |---|views.py
|   |---|utils.py
|   |---|models.py
|---|static   # css, img and js file 
|   |---|css
|   |   |---|styles.css
|   |---|js
|   |   |---|app.js
|   |---|img
|---|templates  # html file
|   |---|index.html
|   |---|layout.hml
|run.py
|requirements.txt 
```



## Add bootstrap

```python
(env) $ pip install flask-bootstrap

#in python file
from flask-bootstrap import Bootstrap
#...
app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route("/bootstrap")
def bootst():
    return render_template("bootstr.html")


#in html file
{% extends "bootstrap/base.html" %}
{% block content %}
<div class="container">
    <h1>this is Bootstrap page</h1>
</div>
{% endblock %}


{% block scripts %}
{{ super() }}
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
{% endblock %}
```

##### Flask-Bootstrap’s base template blocks

| Block name   | Description                                           |
| ------------ | ----------------------------------------------------- |
| doc          | The entire HTML document                              |
| html_attribs | Attributes inside the <html> tag                      |
| html         | The contents of the <html> tag                        |
| head         | The contents of the <head> tag                        |
| title        | The contents of the <title> tag                       |
| metas        | The list of <meta> tags                               |
| styles       | CSS definitions                                       |
| body_attribs | Attributes inside the <body> tag                      |
| body         | The contents of the <body> tag                        |
| navbar       | User-defined navigation bar                           |
| content      | User-defined page content                             |
| scripts      | JavaScript declarations at the bottom of the document |

## Error Pages

```python
# in python file
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

#we crreate 404.html and 500.html file

```

## Add CSS

```css
{% block head %}
{{ super() }}
<link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}"
type="image/x-icon">
<link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}"
type="image/x-icon">
{% endblock %}
```

## Handling  dates and times

```python
(env) $ pip install flask-moment

# python file
from flask-moment import Moment
moment = Moment(app)

#in base.html

    {% block body %}

    {% block scripts %}
    {{ super() }}
    {{ moment.include_moment() }}
    {% endblock %}

    {% endblock %}
#in index.html
{% block body %}

<h1>This is index page</h1>
<p>The local date and time is: {{ moment(current_time).format('LLL') }}.</p>
<p>That was: {{ moment(current_time).fromNow(refresh=True) }}</p>
<p> try this code : {{ current_time }} </p>
<p>The current date and time is: {{ moment(current_time).format('MMMM Do YYYY, h:mm:ss a') }}.</p>

{% endblock %}
```

## Web Forms

##### Simple form

> python file

```python
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/hello',methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)
```

> index.html

```html
{% block body %}
<form action="{{ url_for('hello') }}" method="POST">
    <input type="text" name="name" placeholder=" Enter Your Name">
    <button>
        Submit
    </button>
</form>
{% endblock %}
```

> hello.html

```html
{% block body %}
Hello, {{ name }}
{% endblock %}
```



##### WTForms

```python
(venv) $ pip install flask-wtf

# in python file
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

class LoginForm(FlaskForm):
    username = StringField("enter your Username : ")
    password = PasswordField("enter your Password : ")
    
@app.route("/form", methods=["GET", "POST"])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        return "<h2> username is :  {} <br> and the password is : {} 						</h2>".format(
                    form.username.data, form.password.data
                 )
    return render_template("form.html", form=form)
    
# in html file

 <form action="{{ url_for('form') }}" method="POST">
        {{ form.csrf_token }}
        {{ form.username.label }}
        {{ form.username }} <br>
        {{ form.password.label }}
        {{ form.password }}<br>
        <input type="submit" value="submit">
    </form>
```

##### WTForms standard HTML fields

`BooleanField` : Checkbox with True and False values
`DateField` Text : field that accepts a `datetime.date` value in a given format
`DateTimeField` : Text field that accepts a `datetime.datetime` value in a given format
`DecimalField  `: Text field that accepts a `decimal.Decimal` value
`FileField File` : upload field
`HiddenField` : Hidden text field
`MultipleFileField ` : Multiple file upload field
`FieldList` : List of fields of a given type

`FloatField`  : Text field that accepts a floating-point value
`FormField`  : Form embedded as a field in a container form
`IntegerField`  : Text field that accepts an integer value
`PasswordField`  : Password text field
`RadioField`  : List of radio buttons
`SelectField`  : Drop-down list of choices
`SelectMultipleField`  : Drop-down list of choices with multiple selection
`SubmitField`  : Form submission button
`StringField`  : Text field
`TextAreaField`  : Multiple-line text field

##### WTForms validators

`DataRequired`  :  Validates that the field contains data after type conversion
`Email`  :  Validates an email address
`EqualTo`  :  Compares the values of two fields; useful when requesting a password to be entered twice for
confirmation
`InputRequired`  :  Validates that the field contains data before type conversion
`IPAddress `  : Validates an IPv4 network address
`Length `  : Validates the length of the string entered
`MacAddress`  :  Validates a MAC address
`NumberRange `  : Validates that the value entered is within a numeric range
`Optional`  :  Allows empty input in the field, skipping additional validators
`Regexp`  :  Validates the input against a regular expression
`URL `  : Validates a URL
`UUID `  : Validates a UUID
`AnyOf `  : Validates that the input is one of a list of possible values
`NoneOf `  : Validates that the input is none of a list of possible values

##### Using reCAPTCH IN WTForms

```python
#python file
from flask_wtf import FlaskForm, RecaptchaField
...
app.config["RECAPTCHA_PUBLIC_KEY"] = "6LdzlboUAAAAAHqPF6xaIcHopRX82j4ohEW1WlFQ"
app.config["RECAPTCHA_PRIVATE_KEY"] = "6LdzlboUAAAAAMZbgKBAnAOBZCReWHXMw7S6nwjy"
...
recaptcha = RecaptchaField()

# html file

<form action="{{ url_for('form') }}" method="POST">
            {{ form.csrf_token }}
            {{ form.username.label }}
            {{ form.username }} <br>
            {{ form.password.label }}
            {{ form.password }}<br>
            {{ form.recaptcha }}
            {% for error in form.recaptcha.errors %}
            <ul>
            <li style="color:red;"> {{ error }}</li>
            </ul>
            {% endfor %}
            <input type="submit" value="submit">
        </form>

```

##### Creating a Macro to Reduce Code Duplication

```html
<!-- _render_field.html -->
{% macro render_field(field) %}
{{ field.label }} 
{{ field(**kwargs)|safe }}<!-- (kwargs) keyword argement-->
<ul>
{% for error in field.errors %}
<li style="color:red;"> {{ error }}</li>
{% endfor %}
</ul>
{% endmacro %}

<!-- to use it  -->
{% from "_render_field.html" import render_field %}
...
<form action="{{ url_for('form') }}" method="POST">
{{ form.csrf_token }}
{{ render_field(form.username) }}
{{ render_field(form.password) }}
{{ render_field(form.recaptcha) }}
<input type="submit" value="submit">
</form>
```

##### Using Bootstrap With WTForms

```html
<!-- bootstrap code-->
<form>
  <div class="form-group">
    <label for="exampleInputEmail1">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
    <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
  </div>
  <div class="form-group form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>

<!-- converted code-->
<form action="{{ url_for('form') }}" method="POST">
            {{ form.csrf_token }}
            <div class="form-group">
                <label for="exampleInputEmail1"> {{ form.username.label }}</label>
                {{ form.username(class="form-control", placeholder="Enter email") }}
            </div>
            <div class="form-group">
                <label for="exampleInputEmail1"> {{ form.password.label }}</label>
                {{ form.password(class="form-control", placeholder="Enter email") }}
                <div class="form-group">
                    {{ form.recaptcha }}
                    {% for error in form.recaptcha.errors %}
                    <ul>
                        <li style="color:red;"> {{ error }}</li>
                    </ul>
                    {% endfor %}
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
        </form>
```

##### Validator Error

```python

class LoginForm(FlaskForm):
    #...
    def validate_field(self, field):
        if True:
            raise ValidationError('validation message')

            
#Example:
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), length(min=8, max=16)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

   
    def validate_username(self, username):
        #check if username is in the db 
        user = User.query.filter_by(username=username.data).first()
        # if user exist in db 
        if user:
            raise ValidationError('username already exists. Try another?')
        
        
```



## Linking page

```python
#python code 
@app.route('/more')
def morefun():
    return render_template("more.html")

# in html code
<a href="{{ url_for('morefun') }}">See more... <a/>
```

##  Database

#### Python Database Frameworks 

- in Flask you can work with **MySQL**, **Postgres**, **SQLite**, **Redis**, **MongoDB**, **CouchDB**, or **DynamoDB** if any of
  these is your favorite.
- there are also a number of database abstraction
  layer packages, such as **SQLAlchemy** or **MongoEngine**, that allow you to work at a
  higher level with regular Python objects instead of database entities such as tables,
  documents, or query languages.

###### Facture in  choosing a database

- Ease to Use
- Performance
- Portability
- Flask Integration

#### Flask SQLAlchemy

```python
(env)$ pip install sqlalchemy

#in python file
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app =Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
```



##### Flask-SQLAlchemy database URLs

| Database Engine     | URL                                              |
| ------------------- | ------------------------------------------------ |
| MYSQL               | mysql://username:password@hostname/database      |
| Postgres            | postgresql://username:password@hostname/database |
| SQLite(Linux,macOS) | sqlite:////absolute/path/to/database             |
| SQLite(windows)     | sqlite:///c:/absolute/path/to/database           |

**Ex : **`app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"`

suggests setting key  `SQLALCHEMY_TRACK_MODIFICATIONS` to use less memory 

`app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False`



##### Model 

create a model

```python
class Role(db.Model):
    # SQLAlchemy assign a default table name if you don't assignet
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name
    
    
class User(db.Model):
    __tablename__="users"
    id= db.Column(db.Integer, Primary_key=True)
    username=db.Column(db.String(64), unique=True)

    def __repr__(self):
    
```

###### Create SQL db

```python
(env)$ >> python
from <filename>(ex:hello) import db #model
from apllication import db #package
db.create_all()


#you can use terminal to add data to db


```



##### SQLAlchemy column types

| Type name    | Python type        | Description                                                  |
| ------------ | ------------------ | ------------------------------------------------------------ |
| Integer      | int                | Regular integer, typically 32 bits                           |
| SmallInteger | int                | Short-range integer, typically 16 bits                       |
| BigInteger   | int or long        | Unlimited precision integer                                  |
| Float        | float              | Floating-point number                                        |
| Numeric      | decimal.Decimal    | Fixed-point number                                           |
| String       | str                | Variable-length string                                       |
| Text         | str                | Variable-length string, optimized for large or unbounded length |
| Unicode      | unicode            | Variable-length Unicode string                               |
| UnicodeText  | unicode            | Variable-length Unicode string, optimized for large or unbounded length |
| Boolean      | bool               | Boolean value                                                |
| Date         | datetime.date      | Date value                                                   |
| Time         | datetime.time      | Time value                                                   |
| DateTime     | datetime.datetime  | Date and time value                                          |
| Interval     | datetime.timedelta | Time interval                                                |
| Enum         | str                | List of string values                                        |
| PickleType   | Any python object  | Automatic Pickle serialization                               |
| LargeBinary  | str                | Binary blob                                                  |

##### SQLAlchemy column options

`primary_key`   If set to True , the column is the table’s primary key.
`unique`   If set to True , do not allow duplicate values for this column.
`index`   If set to True , create an index for this column, so that queries are more efficient.
`nullable`   If set to True , allow empty values for this column. If set to False , the column will not allow null values.
`default`   Define a default value for the column.



##### Relationships

###### One To Many Relationship

```python
#  a Role can have Many User
# a User can have One Role


class Role(db.Model):
	__tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # from user table i want to know the user with the same role
    # (backref) is going to create a fake column(role) in the other  				table(User)
	users = db.relationship('User', backref='rol²e' ,lazy='dynamic')
    
    
    
class User(db.Model):
	 __tablename__="users"
    id= db.Column(db.Integer, Primary_key=True)
    username=db.Column(db.String(64), unique=True)
    # the id of the role from roles table
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```

###### One to One Relationships

```python
class Parent(db.Model):
	__tablename__ = "parent"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
	child = db.relationship('Child', backref='parent', uselist=False)
    
    
class Child(db.Model):
	 __tablename__="child"
    id= db.Column(db.Integer, Primary_key=True)
    username=db.Column(db.String(64), unique=True)
	parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))
```

###### Many-To-Many Relationships

```python
# Association table
subs= db.Table('subs',
              db.Column('user_id',db.Integer, db.ForeignKey('user.user_id')),
              db.Column('channel_id',db.Integer, ForeignKey('channel.channel_id')))


# a user can subscribe to many channel
class User(db.model):
    user_id= db.Column(db.Integer, Primary_key=True)
    name = db.Column(db.String(20))
    subscription=db.ralationship('Channel', secondary= subs, backref=db.backref('subscribers', lazy ='dynamic'))
      
               
# a channel can have many users 
class Channel(db.model):
    channel_id= db.Column(db.Integer, Primary_key=True)
    channel_name = db.Column(db.String(20))
```



###### SQLAlchemy relationship options

`backref` Add a back reference in the other model in the relationship.
`primaryjoin` Specify the join condition between the two models explicitly. This is necessary only for 								ambiguous relationships.
`lazy` Specify how the related items are to be loaded. Possible values are select (items are loaded on
			 demand the first time they are accessed), immediate (items are loaded when the source object is
			 loaded), joined (items are loaded immediately, but as a join), subquery (items are loaded
			 immediately, but as a subquery), noload (items are never loaded), and dynamic (instead of loading
			 the items, the query that can load them is given).
`uselist` If set to False , use a scalar instead of a list.
`order_by` Specify the ordering used for the items in the relationship.
`secondary` Specify the name of the association table to use in many-to-many relationships.
`secondaryjoin` Specify the secondary join condition for many-to-many relationships when SQLAlchemy								   cannot determine it on its own.

##### Database Operations

###### Creating the Tables

```python
(env) $ flask shell
>>> from hello import db
>>> db.create_all()
# to destroy all the data of db
>>> db.drop_all()
```

###### Inserting Rows

```sqlite
>>> from hello import Role, User
>>> admin_role = Role(name='Admin')
>>> mod_role = Role(name='Moderator')
>>> user_role = Role(name='User')
>>> user_john = User(username='john', role=admin_role)
>>> user_susan = User(username='susan', role=user_role)
>>> user_david = User(username='david', role=user_role)

>>> db.session.add(admin_role)
>>> db.session.add(mod_role)
>>> db.session.add(user_role)
>>> db.session.add(user_john)
>>> db.session.add(user_susan)
>>> db.session.add(user_david)
or
>>> db.session.add_all([admin_role, mod_role, user_role,
... user_john, user_susan, user_david])

>>> db.session.commit()
```

###### Modifying Rows

```sqlite
>>> admin_role.name = 'Administrator'
>>> db.session.add(admin_role)
>>> db.session.commit()
```

###### Deleting Rows

```sqlite
>>> db.session.delete(mod_role)
>>> db.session.commit()
```

###### Querying Rows

```sqlite
>>> Role.query.all()
[<Role 'Administrator'>, <Role 'User'>]
>>> User.query.all()
[<User 'john'>, <User 'susan'>, <User 'david'>]


>>> User.query.filter_by(role=user_role).all()
[<User 'susan'>, <User 'david'>]
```

###### SQLAlchemy query filters

`filter()` Returns a new query that adds an additional filter to the original query
`filter_by()` Returns a new query that adds an additional equality filter to the original query
`limit()` Returns a new query that limits the number of results of the original query to the given number
`offset()` Returns a new query that applies an offset into the list of results of the original query
`order_by()` Returns a new query that sorts the results of the original query according to the given criteria
`group_by()` Returns a new query that groups the results of the original query according to the given criteria

###### SQLAlchemy query executors

`all()` Returns all the results of a query as a list
`first()` Returns the first result of a query, or None if there are no results
`first_or_404()` Returns the first result of a query, or aborts the request and sends a 404 error as the 									response if there are no results
`get()` Returns the row that matches the given primary key, or None if no matching row is found
`get_or_404()` Returns the row that matches the given primary key or, if the key is not found, aborts the 								request and sends a 404 error as the response
`count()` Returns the result count of the query
`paginate()` Returns a Pagination object that contains the specified range of results

```sql
>>> users = user_role.users
>>> users
[<User 'susan'>, <User 'david'>]
>>> users[0].role
<Role 'User'>


>>> user_role.users.order_by(User.username).all()
[<User 'david'>, <User 'susan'>]
>>> user_role.users.count()
2
```



#### Code for Test

> python file

```python
@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username=form.name.data)
			db.session.add(user)
			db.session.commit()
			session['known'] = False
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
	return render_template('index.html',
		form=form, name=session.get('name'),
		known=session.get('known', False))
```

> html file

```html
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}
{% block title %}Flasky{% endblock %}
{% block page_content %}
<div class="page-header">
<h1>
    Hello, 
    {% if name %}
    {{ name }}
    {% else %}
    Stranger
    {% endif %}
    !</h1>
{% if not known %}
<p>Pleased to meet you!</p>
{% else %}
<p>Happy to see you again!</p>
{% endif %}
</div>
{{ wtf.quick_form(form) }}
{% endblock %}
```

## Flask Migrate

if i want to add new column to table in my database flask migrate compare the current version off your database with the old one and make changes . 

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.ralationship('Pet', backref ='owner', lazy='dynamic')

class Pet(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    new = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
```

> (env) $ pip install flask-migrate

```python
from flask_migrate import Migrate
...
migrate = Migrate(app, db)
```

##### Initialize 

This commend create a  **migrations directory**   where all the migration scripts will be
stored.

```
(env) $ flask db init
```

##### Create a Migration Script

```
(env) $ flask db migrate -m"initial megration"
```

##### Updating a Migrate 

```
(env) $ flask db update
```

### Using Flask-Script

> menage.py

```python
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
...

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
```

```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python manage.py db --help
```



## Flask-Mail

Many types of applications need to notify users when certain events occur, and the
usual method of communication is email.

we are going to learn how to send emails from a Flask application.



##### Install Flask-Mail

```
(env) $ pip install flask-mail
```

###### Flask-Mail SMTP server configuration keys

| Key           | Default   | Description                                   |
| ------------- | --------- | --------------------------------------------- |
| MAIL_SERVER   | localhost | Hostname or IP address of the email server    |
| MAIL_PORT     | 25        | Port of the email server                      |
| MAIL_USE_TLS  | Fase      | Enable Transport Layer Security(TLS) Security |
| MAIL_USE_SSL  | Flase     | Enable Secure Sockets Layer (SSL) Security    |
| MAIL_USERNAME | None      | Mail Account username                         |
| MAIL_PASSWORD | None      | Mail Account password                         |

###### Configuration

**In Python File** 

```python
from flask_mail import Mail
import os
# ...
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = ('Ismail Fiki','contact@ismailfiki.com')
app.config['MAIL_MAX_EMAILS'] = None

#Flask-Mail is initiation

mail = Mail(app)
```

> Never write account credentials directly in your scripts, particularly
> if you plan to release your work as open source. To protect your
> account information, have your script import sensitive information
> from environment variables.



Set Up Server And Send Email

```python
from flask_mail import Mail, Message
...
@app.route('/')
def index():
    msg = Message('Hey There', recipients=['sendto@mail.com'])
    # to add more recipient
    msg.add_recipient('sendto3@mail.com','sendto2@mail.com')
    #you can use msg.body or msg.html don't use them both at the same time
    msg.body = 'message body '
    msg.html = '<b> this is the message on html </b>'
    mail.send(msg)
    return 'Message has been sent!'
```



###### Integrate Email With The App

```python
from flask_mail import Message
...
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
    	sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
```

```python
# ...
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
# ...
@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
    	user = User.query.filter_by(username=form.name.data).first()
    if user is None:
    	user = User(username=form.name.data)
    	db.session.add(user)
    	session['known'] = False
    	if app.config['FLASKY_ADMIN']:
    		send_email(app.config['FLASKY_ADMIN'], 'New User',
    			'mail/new_user', user=user)
    else:
    	session['known'] = True
    session['name'] = form.name.data
    form.name.data = ''
    return redirect(url_for('index'))
return render_template('index.html', form=form, name=session.get('name'),
    	known=session.get('known', False))
```

# Package Structure

```
flasky
	packagename
	___|templates
	___|static
	___|__init__.py
	___|rootes.py
	___|forms.py
	___|models.py
	env
	run.py
```

```
to create a db
python
>> from packagename import db
>> from packagename.models import <class names>
>>db.create_all()

```



## Flash Notification

`rootes.py`

```python
from flask import flash
# passing the message and class for bbotstrap to use
flash(f'Your Account has been created ! You are now able to log in ', 'success')

```

in `base.html`

```html
 <div class="col-md-8">
                <!-- create an alert for flash message using bootstrap -->
                {% with messages = get_flashed_messages(with_categories =true) %}
                {% if messages %}
                {% for category, message in messages %}
                <div class="alert alert-{{ category }} ">
                    {{ message }}
                </div>
                {% endfor %}
                {% endif %}
                {% endwith %}
                {% block content %}{% endblock %}
            </div>
```



## Large Application Structure

```
flasky
	app
	___|templates
	___|static
	___|main
	_______|__init__.py
	_______|errors.py
	_______|forms.py
	_______|views.py
	___|__init__.py
	___|email.py
	___|models.py
	migrations
	tests
	___|__init__.py
	___|test*.py
	env
	requirements.txt
	config.py
	flasky.py
```

## Security

### Bcrypt

```python
pip install flask-bcrypt




#create hash code in register for example
hashed_password = bcrypt.generate_password_hash(<password>).decode('utf-8')
#check if the password we have is equil to the password we entred
bcrypt.check_password_hash(hashed_password,<pass>)

```

in  `__init__.py ` file

```python
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
```

## flask-login

```python
pip install flask-login

#initialisation
# in __init__.py
from flask_login import LoginLanager

#...
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# in models.py
from <packagename> import db,login_manager


# EXAMPLE:

# in models.py
#****************

from flaskblog import db, login_manager
from flask_login import UserMixin

# create a decorated function to connect to db
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    #....

# in roores.py
#****************
from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # check if the email exist
        user = User.query.filter_by(email=form.email.data).first()
        # check if the email and password is valid
        if user and bcrypt.check_password_hash(user.password, 						form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check your Email and 						password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account' )

```

#### CRUD

###### Create

> rootes.py

```python
@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)



@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data,
                        content=form.content.data, author=current_user)
        # add the user to db
        db.session.add(new_post)
        # commit change
        db.session.commit()
        flash('Your Post has been created', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', legend='New Post', form=form)
```

> forms.py

```python
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
```

> create_post.html

```html
{% extends 'layout.html' %}



{% block content %}
<div class="content-section">
    <form method="POST" action="">
        {{ form.hidden_tag() }}
        <fieldset class="form-group">
        <legend class="border-bottom mb-4">{{ legend }} </legend>
        <div class="form-group">
        {{ form.title.label(class="form-control-label") }}
        {% if form.title.errors %}
        {{ form.title(class="form-control form-control-lg is-invalid") }}
         <div class="invalid-feedback">
        {% for error in form.title.errors %}
         <span>{{ error }}</span>
        {% endfor %}
                    </div>
        {% else %}
        {{ form.title(class="form-control form-control-lg") }}
         {% endif %}
            </div>
            <div class="form-group">
        {{ form.content.label(class="form-control-label") }}
        {% if form.content.errors %}
       {{ form.content(class="form-control form-control-lg is-invalid") }}
                    <div class="invalid-feedback">
                        {% for error in form.content.errors %}
                            <span>{{ error }}</span>
                        {% endfor %}
                    </div>
                {% else %}
                    {{ form.content(class="form-control form-control-lg") }}
                {% endif %}
            </div>
        </fieldset>
        <div class="form-group">
            {{ form.submit(class="btn btn-outline-info") }}
        </div>
    </form>
</div>
{% endblock %}
```

> layout.html

```html
...
{% if current_user.is_authenticated %}
<a class="nav-item nav-link" href="{{ url_for('new_post') }}">New Post</a>
...
 {% endif %}
```

###### Update

> post.html

```html
{% extends 'layout.html' %}

{% block content %}

<article class="media content-section">
  <img class="rounded-circle article-img" src="{{ url_for('static', filename='image/'+post.author.image_file) }}">
  <div class="media-body">
    <div class="article-metadata">
      <a class="mr-2" href="#">{{ post.author.username }}</a>
      <small class="text-muted">{{ post.date_posted.strftime('%Y-%m-%d at %H:%M:%S') }}</small>
      {% if post.author == current_user %}
      <div>
        <a class="btn btn-secondary btn-sm mt-1 mb-1" href="{{ url_for('update_post', post_id=post.id) }}"> Update </a>
        <button type="button" class="btn btn-danger btn-sm m-1" data-toggle="modal" data-target="#deletModal">Delete
        </button>
        <!-- Modal -->
        <div class="modal fade" id="deletModal" tabindex="-1" role="dialog" aria-labelledby="deletModalLabel"
          aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="deletModalLabel">Delet Post</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <!-- <div class="modal-body">
                Are you Sure you want to Delete this Post ?
              </div> -->
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <form action="{{ url_for('delete_post',post_id=post.id) }}" method="post">
                  <input type="submit" class="btn btn-danger" value="Delete">
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
      {% endif %}
    </div>
    <h2 class="article-title">{{ post.title }}</h2>
    <p class="article-content">{{ post.content }}</p>
  </div>
</article>

{% endblock %}
```



> rootes.py

```python
@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    #get the post with id= post_id or 404 page
    post = Post.query.get_or_404(post_id)
    #if the author of the post != the current user 
    if post.author != current_user:
        # forbieden page 
        abort(403)
    form = PostForm()
    if form.validate():
        post.title = form.title.data
        post.content = form.content.data

        db.session.commit()
        flash('Your Post has been Updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    return render_template('create_post.html', title='Update Post', legend='Update Post', form=form)

```

###### Delete

> rootes.html

```python
@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
     #get the post with id= post_id or 404 page
    post = Post.query.get_or_404(post_id)
    #if the author of the post != the current user 
    if post.author != current_user:
        # forbieden page 
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your Post has been Deleted!', 'warning')
    return redirect(url_for('home'))
```

#### Pagination

```python
# 1 rootes.py
@app.route('/')
@app.route('/home')
def home():
    #get the 'page' with default=1 and accept only int
    page = request.args.get('page',1,type = int)            # Add this
    posts = Post.query.all() 								# Remove this
    #paginare 5 post per page
    posts = Post.query.paginate(page =page, per_page=5)     # Add this
    return render_template('home.html', posts=posts)


# 2 home.html
{% for post in posts %}                              # Remove this
{% for post in posts.items %}                        # Add this
...
#in the end of the page we add this code
{% for page_num in posts.iter_pages(left_edge=1, right_edge=1, left_current=1, right_current=2) %}
{% if page_num %}
    <!-- if we are in the curreet page -->
    {% if posts.page == page_num %}
    <!-- fill this btn -->
    <a class="btn btn-info mb-4" href="{{ url_for('home',page=page_num) }}"> {{ page_num }} </a>
    {% else %}
    <a class="btn btn-outline-info mb-4" href="{{ url_for('home',page=page_num) }}"> {{ page_num }} </a>
    {% endif %}

{% else %}
...
{% endif %}
{% endfor %}
```

#### Order Post 

```python
# order post from the wenest to the last 
posts = Post.query
.order_by(Post.date_posted.desc())
.paginate(page =page, per_page=5)

```

#### Display post by User

```python
 # 1 create a root for user post
    # roots.py
    @app.route('/user/<string:username>')
def user_posts(username):
    #get the 'page' with default=1 and accept only int
    page = request.args.get('page',1,type = int)
    # grab the post by user
    user = User.query.filter_by(username=username).first_or_404()
    #filter post by username if one is found 
    #paginare 5 post per page
    posts = Post.query\
        .filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page =page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


# 2  create a view for this 
	# user_posts.html
    
{% extends 'layout.html' %}

{% block content %}

<h1 class="mb-3"> Posts by : {{ user.username }} ({{ posts.total }}) </h1>
{% for post in posts.items %}
<article class="media content-section">
<img class="rounded-circle article-img" src="{{ url_for('static', filename='image/'+post.author.image_file) }}">
    <div class="media-body">
        <div class="article-metadata">
            <a class="mr-2" href="{{ url_for('user_posts', username = post.author.username) }}">{{ post.author.username }}</a>
            <small class="text-muted">{{ post.date_posted.strftime('%Y-%m-%d') }}</small>
        </div>
        <h2><a class="article-title" href="{{ url_for('post', post_id=post.id) }}">{{ post.title }}</a></h2>
        <p class="article-content">{{ post.content }}</p>
    </div>
</article>
{% endfor %}
{% for page_num in posts.iter_pages(left_edge=1, right_edge=1, left_current=1, right_current=2) %}
{% if page_num %}
    <!-- if we are in the curreet page -->
    {% if posts.page == page_num %}
    <!-- fill this btn -->
    <a class="btn btn-info mb-4" href="{{ url_for('user_posts', username=user.username ,page=page_num) }}"> {{ page_num }} </a>
    {% else %}
    <a class="btn btn-outline-info mb-4" href="{{ url_for('user_posts', username=user.username ,page=page_num) }}"> {{ page_num }} </a>
    {% endif %}

{% else %}
...
{% endif %}
{% endfor %}

{% endblock %}
```

## Email and Password Reset

use Email to allow users to reset there password



### Generate   Secure Token

```python
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
#Generate token expire time is 30 seconds
s = Serializer('secret',30)
token = s.dumps({'user_id':1}).decode('utf-8')
token
'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU3MTU3MDM0NiwiZXhwIjoxNTcxNTcwMzc2fQ.eyJ1c2VyX2lkIjoxfQ.Z92_ZiQlACUts_3Fg49EXcZhSAuEMyWEU_QzLzvBhT6QC-ae8yqwZc91YZNIi16UVbhLpuRnagGVJqRnGz-F1A'
# if we load this after 30second it giv's an error
s.loads(token)
{'user_id': 1}
```

##### Create Validation Methods

```python
# models.py
# 

from flaskblog import db, login_manager, app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class User(db.Model, UserMixin):
	...
    # generate rest token
    def get_rest_token(self, expire_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expire_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')
    
    
    @staticmethod # not to expect the (self) as an argement
    def verify_reset_token(token):  
        s=Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    	...
```



##### Create roots for user to Reset Password

###### Create a Form

```python
class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        # check if email is in the db
        user = User.query.filter_by(email=email.data).first()
        # if email don't exist in db
        if user is None:
            raise ValidationError(
                'There is no account with that email. You must register first!')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[
                             DataRequired(), length(min=8, max=16)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
```

###### Create rootes

```python
#__init__.py


import os
...
from flask_mail import Mail


app = Flask(__name__)
...
# Mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
...
mail = Mail(app)
...


from flaskblog import rootes



#rootes.py
def send_rest_email(user):
    token = user.get_rest_token()
    msg = Message('Password Reset Request',
                  sender='smailfiki0808@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password visit the following link: 
    { url_for('reset_password' , token =token , _external=True) } 

    If you did not make this request then simply ignor this Email and no changes made
    '''
    mail.send(msg)


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    # if we login then redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    # if we submit the form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_rest_email(user)
        flash('An Email has been sent with instruction to Reset password!', 'info')
        return redirect(url_for('login'))

    return render_template('reset_request.html', title='Request Reset Password', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
     # if we login then redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)  # user =user.id
    if user is None:
        flash('that is an invalid or expired token!', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # generate a hash for the password entred
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user.password = hashed_password
        # commit change
        db.session.commit()
        # notification the user that the account is created successfully
        flash(f'Your Password has been Updated ! You are now able to log in ', 'success')
        # sent the user to the login page to log in
        return redirect(url_for('login'))
    return render_template('reset_password.html', title='Reset Password', form=form)
```



## Structure the project

### Blueprints

#### Create packages

```python
#main package
flaskblog
	# sub package
	main
		__init.py
		rootes.py
	# sub package
	users
		__init.py
		rootes.py
		forms.py
	# sub package
    posts
		__init.py
		rootes.py
		forms.py
	__init__.py
	models.py
	site.db
    config.py
	# img, css and js file
    static
	# html file
    templates
run.py
requirements.txt
```

#### Add Blueprint

**1** - in **sub packages** `rootes.py`  we add this code

```python
from flask import Blueprint
<subpackage name> = Blueprint('<subpackage name>', __name__)

# change the @app.route   with @<subpackage name>.route
```

**2** - change the `__init__.py` in the **main package**

```python
#...
#
from <main package name>.<subpackage name>.rootes import <subpackage name>
#...
app.register_blueprint(<subpackage name>)
```

**3** - change `url_for()` in the `html` and `py` files

```python
# change the url_for()
url_for('home') => url_for('<subpackage name>.home')
```

####  Config file

create `config.py` file 

```python
import os

class Config: 
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # Mail config
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = '6aa1b105d5f87a'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = 'c2eded0939c1de'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
```

in the `__ini__t.py` of the **main package**

```python
from flaskblog.config import Config


app = Flask(__name__)
app.config.from_object(Config)
```

#### Create_app function



**1** - `__init__.py` **before change** 

```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from flaskblog import routes
```



`__init__.py` **After change** 

```python


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()
login_manager = LoginManager()
# the function to redirect if we attemp to access login_required view
login_manager.login_view = 'users.login'
# customize message category if we attemp to access login_required view
login_manager.login_message_category = 'info'




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    from flaskblog.users.rootes import users
    from flaskblog.posts.rootes import posts
    from flaskblog.main.rootes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app


```

**2** -   **change** `app` to `current_app` in all the file  except `__init__.py` in the **main package**  

**3** -  change the `run.py`

**Before**

```python
from flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)
```

**After**

```python

from flaskblog import create_app

app = create_app()
if __name__ == "__main__":
    app.run(debug=True)

```



### Errors Handlers

create a sub package errors with  `__init__.py` and `handlers.py`

```python
# in handlers.py 
from flask import Blueprint , render_template


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(403)
def error_300(error):
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500

```

in the **templates folder** we add **errors folder** and `403.html, 404.html and 500.html` pages inside it

## Unit testing

```
$ tree
├── instance
├── migrations
├── project
│   ├── __init__.py
│   ├── models.py
│   ├── recipes
│   ├── static
│   ├── templates
│   ├── tests
│   │   ├── test_basic.py
│   │   ├── test_recipes.py
│   │   └── test_users.py
│   └── users
├── requirements.txt
└── run.py
```

### Creating a Basic Unit Test File

```python
# project/test_basic.py
 
 
import os
import unittest
 
from project import app, db, mail
 
 
TEST_DB = 'test.db'
 
 
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
        # Disable sending emails during unit testing
        mail.init_app(app)
        self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
 
###############
#### tests ####
###############
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
 
if __name__ == "__main__":
    unittest.main()
```

run this code to lunch the test :`python project/tests/test_basic.py` 

# Flask + PostgreSQL

https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc

https://github.com/dushan14/books-store

https://github.com/dushan14/books-store.git

*Note that if you created the* **name_of_user** *and* **name_of_database** *as your user name on your machine, you can access that database with that user with* `psql` *command.*

```python
# Now create a superuser for PostgreSQL 
-u postgres createuser --superuser name_of_user
# And create a database using created user account 
-u name_of_user createdb name_of_database
# You can access created database with created user by, 
psql -U name_of_user -d name_of_database
```

## sample code with Flask 

`app.py`

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/name/<name>")
def get_book_name(name):
    return "name : {}".format(name)

@app.route("/details")
def get_book_details():
    author=request.args.get('author')
    published=request.args.get('published')
    return "Author : {}, Published: {}".format(author,published)

if __name__ == '__main__':
    app.run()
```

## Create database

First create the database we need here for our application named **books_store**

```
-u name_of_user createdb books_store
```

Now you can check the created database with,

```
psql -U name_of_user -d books_store
```

## Create configurations

`config.py`

```python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
```

According to created configurations set **“APP_SETTINGS”** environment variable by running this in the terminal

```
export APP_SETTINGS="config.DevelopmentConfig"
```

Also add **“DATABASE_URL”** to environment variables. In this case our database URL is based on the created database. So, export the environment variable by this command in the terminal,

```
export DATABASE_URL="postgresql://localhost/books_store"
```

## Database migration

```
pip install flask_sqlalchemy
```

in `app.py`

```python
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy # Add this

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS']) # Add this
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Add this
db = SQLAlchemy(app) # Add this

from models import Book # Add this

@app.route("/")
def hello():
    return "Hello World!"
```

`models.py`

> *Note that* **serialize** *method here is not needed for database migration but it will be useful when we need to return book objects in response as JSON.*

```python
from app import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.String())

    def __init__(self, name, author, published):
        self.name = name
        self.author = author
        self.published = published

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'author': self.author,
            'published':self.published
```

`manage.py`

```
pip install flask_script
pip install flask_migrate
pip install psycopg2-binary
```



```python
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
```

Now we can start migrating database. First run,

```
python manage.py db init
```

This will create a folder named **migrations** in our project folder. To migrate using these created files, run

```
python manage.py db migrate
```

Now apply the migrations to the database using

```
python manage.py db upgrade
```

> *In a case of migration fails to be success try droping auto generated* **alembic_version** *table by* `drop table alembic_version;`

##  Finish the code

`app.py`

```python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Book

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add")
def add_book():
    name=request.args.get('name')
    author=request.args.get('author')
    published=request.args.get('published')
    try:
        book=Book(
            name=name,
            author=author,
            published=published
        )
        db.session.add(book)
        db.session.commit()
        return "Book added. book id={}".format(book.id)
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        books=Book.query.all()
        return  jsonify([e.serialize() for e in books])
    except Exception as e:
	    return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        book=Book.query.filter_by(id=id_).first()
        return jsonify(book.serialize())
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run()
```

Also, as now we have created **manage.py** now we can run our server locally by,

```
python manage.py runserver
```

`getdata.html`

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
        crossorigin="anonymous">
</head>

<body>
    <div class="container">

        <div class="container">
            <br>
            <br>

            <div class="row align-items-center justify-content-center">
                <h1>Add a book</h1>
            </div>
            <br>

            <form method="POST">

                <label for="name">Book Name</label>
                <div class="form-row">
                    <input class="form-control" type="text" placeholder="Name of Book" id="name" name="name">
                </div>
                <br>
                <div class="form-row">
                    <label for="author">Author</label>
                    <input class="form-control" type="text" placeholder="Author Name" id="author" name="author">
                </div>
                <br>
                <div class="form-row ">
                    <label for="published">Published</label>
                    <input class="form-control " type="date" placeholder="Published" id="published" name="published">
                </div>

                <br>
                <button type="submit " class="btn btn-primary " style="float:right ">Submit</button>
            
            </form>
            <br><br>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js " integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo "
        crossorigin="anonymous "></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js " integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49 "
        crossorigin="anonymous "></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js " integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy "
        crossorigin="anonymous "></script>
</body>

</html>
```

