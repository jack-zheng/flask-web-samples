from flask import Flask, render_template, flash, redirect, url_for
from flask import session, send_from_directory, request
from forms import LoginForm, UploadForm, MultiUploadForm, RichTextForm
from forms import NewPostForm, SigninForm, RegisterForm
from forms import SigninForm2, RegisterForm2
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError
from flask_ckeditor import CKEditor
import os
import uuid


app = Flask(__name__)
# just for testing, set it to .env file when production env
app.secret_key = 'secret04'
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
app.config['ALLOWED_EXTENSIONS'] = ['png', 'jpg', 'jpeg', 'gif']
app.config['CHEDITOR_SERVE_LOCAL'] = True

ckeditor = CKEditor(app)


@app.route('/dropzone-upload', methods=['GET', 'POST'])
def dropzone_upload():
    pass


@app.route('/custom-validator', methods=['GET', 'POST'])
def custom_validator():
    pass


@app.route('/multi-form', methods=['GET', 'POST'])
def multi_form():
    signin_form = SigninForm()
    register_form = RegisterForm()

    if signin_form.submit1.data and signin_form.validate():
        username = signin_form.username.data
        flash('%s, you just submit the signin form.' % username)
        return redirect(url_for('index'))

    if register_form.submit2.data and register_form.validate():
        username = register_form.username.data
        flash('%s, you just submit the register form.' % username)
        return redirect(url_for('index'))

    return render_template(
        '2form.html', signin_form=signin_form, register_form=register_form)


@app.route('/multi-form-multi-view')
def multi_form_multi_view():
    signin_form = SigninForm2()
    register_form = RegisterForm2()
    return render_template(
        '2form2view.html', signin_form=signin_form, register_form=register_form
    )


@app.route('/handle-signin', methods=['POST'])
def handle_signin():
    signin_form = SigninForm2()
    register_form = RegisterForm2()

    if signin_form.validate_on_submit():
        username = signin_form.username.data
        flash('%s, you just submit the Signin Form.' % username)
        return redirect(url_for('index'))

    return render_template(
        '2form2view.html',
        signin_form=signin_form, register_form=register_form)


@app.route('/handle-register', methods=['POST'])
def handle_register():
    signin_form = SigninForm2()
    register_form = RegisterForm2()

    if register_form.validate_on_submit():
        username = register_form.username.data
        flash('%s, you just submit the Register Form.' % username)
        return redirect(url_for('index'))
    return render_template(
        '2form2view.html',
        signin_form=signin_form, register_form=register_form)


@app.route('/two-submits', methods=['GET', 'POST'])
def two_submits():
    form = NewPostForm()
    if form.validate_on_submit():
        if form.save.data:
            print('Save post')
            flash('You click the save button')
        elif form.publish.data:
            print('Publish post')
            flash('You click the publish button')
        return redirect(url_for('index'))
    return render_template('2submit.html', form=form)


@app.route('/ckeditor', methods=['GET', 'POST'])
def integrate_ckeditor():
    form = RichTextForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        flash('Your post is published.')
        return render_template('post.html', title=title, body=body)
    return render_template('ckeditor.html', form=form)


@app.route('/multi-upload', methods=['GET', 'POST'])
def multi_upload():
    form = MultiUploadForm()

    if request.method == 'POST':
        filenames = []
        try:
            validate_csrf(form.csrf_token.data)
        except ValidationError:
            flash('CSRF token error')
            return redirect(url_for('multi_upload'))

        if 'photo' not in request.files:
            flash('This field is required.')
            return redirect(url_for('multi_upload'))

        for f in request.files.getlist('photo'):
            if f and allowed_file(f.filename):
                filename = random_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
                filenames.append(filename)
            else:
                flash('Invalid file type')
                return redirect(url_for('multi_upload'))
        flash('Upload success.')
        session['filenames'] = filenames
        return redirect(url_for('show_images'))
    return render_template('upload.html', form=form)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/uploads/<path:filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


@app.route('/uploaded-images')
def show_images():
    return render_template('uploaded.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = random_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('Upload success.')
        session['filenames'] = [filename]
        return redirect(url_for('show_images'))
    return render_template('upload.html', form=form)


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename


@app.route('/html')
def html():
    return render_template('pure_html.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/basic')
def basic():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        flash('Welcome home, %s!' % username)
        return redirect(url_for('index'))
    return render_template('basic.html', form=form)


@app.route('/bootstrap', methods=['GET', 'POST'])
def bootstrap():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        flash('Welcome home, %s!' % username)
        return redirect(url_for('index'))
    return render_template('bootstrap.html', form=form)
