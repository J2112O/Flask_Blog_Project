from flask import render_template, url_for, flash, redirect
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from app import app

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))  # Again the route funtion, not the route url
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed.', 'danger')
    return render_template('login.html', title='Login', form=form)
