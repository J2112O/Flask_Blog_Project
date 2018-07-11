from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f403e46e3971c34161fa8dac8649968a'
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


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
