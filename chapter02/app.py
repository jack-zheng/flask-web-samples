from flask import Flask, request, redirect, jsonify
from flask import make_response, url_for, session, abort
from datetime import datetime
from urllib.parse import urlparse, urljoin
from jinja2.utils import generate_lorem_ipsum


app = Flask(__name__)
# just for testing, set it to .env file when production env
app.secret_key = 'secret'


@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=2)
    return '''
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <h1>Very long post</h1>
    <div class="body">%s</div>
    <button id="load">Load More</button>
    <script type="text/javascript">
    $( "#load" ).click(function() {
        $.ajax({
                    url: '/more',
                    type: 'get',
                    success: function(data){
                        $('.body').append(data);
                    }
                })
    });
    </script>
    ''' % post_body


@app.route('/more')
def load_post():
    return generate_lorem_ipsum(n=1)


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


@app.route('/bar')
def bar():
    return '<h1>Foo5101</h1><a href="%s">Do something and redirect</a>'\
        % url_for('do_something', next=request.full_path)


def redirect_back(default='hello', **kwargs):
    print('next value: %s' % request.args.get('next'))
    for target in request.args.get('next'), request.referrer:
        if target:
            print('target = %s' % target)
            if is_safe_url(target):
                return redirect(target)
    return redirect(url_for(default, **kwargs))


@app.route('/do_something_and_redirect')
def do_something():
    print("Into do something method")
    return redirect_back()


@app.route('/referrer')
def test_refer():
    return '<h1>Referrer Test</h1><a href="%s">Go to bar page</a>'\
        % url_for('bar', next=request.full_path)


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    print('request host url: %s' % request.host_url)
    print('netloc = %s | %s' % (ref_url.netloc, test_url.netloc))
    return test_url.scheme in ('http', 'https') and \
        ref_url.netloc == test_url.netloc
