from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

moment = Moment(app)
Bootstrap(app)


class RegisterForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(1, 20)])
    email = StringField(
        'Email', validators=[DataRequired(), Email(), Length(1, 20)])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(8, 128)])
    submit = SubmitField('Register')


@app.route('/bootstrap')
def bootstrap():
    form = RegisterForm()
    return render_template('bootstrap.html', form=form)


@app.route('/')
def index():
    return render_template('index.html', time=datetime.utcnow())


@app.shell_context_processor
def make_shell_context():
    return dict(moment=moment)
