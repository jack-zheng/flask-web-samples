from flask import Flask, render_template, Markup, flash, redirect, url_for


app = Flask(__name__)
# just for testing, set it to .env file when production env
app.secret_key = 'secret'
app.context_processor(lambda: dict(rmb='100yuan'))

user = {
    'username': 'Jack',
    'bio': 'A boy who wanna to be hacker'
}

movies = [
    {'name': 'Movie01', 'year': '1990'},
    {'name': 'Movie02', 'year': '1991'},
    {'name': 'Movie03', 'year': '1992'},
    {'name': 'Movie04', 'year': '1993'},
    {'name': 'Movie05', 'year': '1994'},
    {'name': 'Movie06', 'year': '1995'},
]


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.template_filter()
def musical(s):
    return s + Markup(' &#9835;')


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.context_processor
def inject_foo():
    foo = 'I am foo'
    return dict(foo=foo)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/flash')
def just_flash():
    flash('I am flash, who is looking for me?')
    return redirect(url_for('index'))
