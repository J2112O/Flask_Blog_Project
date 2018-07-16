from flask import render_template, url_for, flash, redirect
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from app import app, db, bcrypt
from flask_login import login_user

posts = [
    {
        'author': 'Some Author',
        'title': 'Blog Post 1',
        'content': 'First blog post',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Another Author',
        'title': 'Blog Post 2',
        'content': 'Second blog post',
        'date_posted': 'May 21, 2013'
    },
    {
        'author': 'What an Author',
        'title': 'Blog Post 3',
        'content': 'Third blog post for your mother',
        'date_posted': 'May 28, 2010'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')  # decode() makes it a string and not in bytes
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))  # Again the route funtion, not the route url
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # Getting form data here remember
        if user and bcrypt.check_password_hash(user.password, form.password.data):  # checking the password in the db against the password from the template form
            login_user(user, remember=form.remember.data)  # function takes the Remember me tic box from the form if there is a match
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and/or password.', 'danger')
    return render_template('login.html', title='Login', form=form)
