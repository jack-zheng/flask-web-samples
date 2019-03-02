from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms import IntegerField
from flask_wtf.file import FileField, FileRequired, FileAllowed


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
