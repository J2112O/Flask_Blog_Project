from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
