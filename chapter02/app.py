from flask import Flask, request, redirect, jsonify
from flask import make_response, url_for, session, abort
from datetime import datetime

app = Flask(__name__)
# just for testing, set it to .env file when production env
app.secret_key = 'secret'


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))


@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return 'Welcome to admin page.'


@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello'))


@app.route('/set/<name>')
def set_cookie(name):
    resp = make_response(redirect(url_for('hello')))
    resp.set_cookie('name', name)
    return resp


@app.before_request
def log_time():
    print('log time before request: %s' % datetime.utcnow())


@app.route('/hello')
def hello():
    # args.get(key1, key2), key2 - default value
    name = request.args.get('name')
    if name is None:
        print('No name from URL, use cookie')
        name = request.cookies.get('name', 'COOOOKIEs')

    resp = '<h1>Chapter02, %s!<h1>' % name
    if 'logged_in' in session:
        resp += ' [Authenticated]'
    else:
        resp += ' [Not Authenticated]'
    return resp


@app.route('/testp', methods=['GET', 'POST'])
def testp():
    return '<h1>Test Post Method!</h1>'


# Corrigendum, miss /
@app.route('/goback/<int:year>')
def go_back(year):
    return '<p>Welcome to %d!</p>' % (2019-year)

# Corrigendum, miss '"'
@app.route('/colors/<any("blue", "red", "white"):color>')
def three_colors(color):
    return '<p>Pick color： %s</p>' % color


# Corrigendum: using {:} instead of {,}
# only when the code is 302, the redirect will be triggered
@app.route('/redirect01')
def redirect01():
    return '', 302, {'Location': 'http://bing.com'}


@app.route('/redirect02')
def redirect02():
    return redirect('http://baidu.com')


@app.route('/foo')
def foo():
    return jsonify(name='jack', age='20')
