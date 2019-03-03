from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError, Email
from wtforms import IntegerField, MultipleFileField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_ckeditor import CKEditorField


class SigninForm2(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(8, 128)])
    submit = SubmitField('Sign in')


class RegisterForm2(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(1, 20)])
    email = StringField(
        'Email', validators=[DataRequired(), Email(), Length(1, 20)])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(8, 128)])
    submit = SubmitField('Register')


class SigninForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(8, 128)])
    submit1 = SubmitField('Sign in')


class RegisterForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(1, 20)])
    email = StringField(
        'Email', validators=[DataRequired(), Email(), Length(1, 20)])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(8, 128)])
    submit2 = SubmitField('Register')


class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = TextAreaField('Body', validators=[DataRequired()])
    save = SubmitField('Save')
    publish = SubmitField('Publish')


class RichTextForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Publish')


class MultiUploadForm(FlaskForm):
    photo = MultipleFileField('Upload Image', validators=[DataRequired()])
    submit = SubmitField()


class UploadForm(FlaskForm):
    photo = FileField(
        'Upload Image', validators=[
            FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField()


class LoginForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired()])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


class FortyTwoForm(FlaskForm):
    answer = IntegerField('The Number')
    submit = SubmitField()

    def validate_answer(form, field):
        if field.data != 42:
            raise ValidationError('Must be 42.')


# define a global validation
def is_42(form, field):
    if field.data != 42:
        raise ValidationError('Must be 42.')


class FortyTwoForm_2(FlaskForm):
    answer = IntegerField('The Number', validators=[is_42])
    submit = SubmitField()
