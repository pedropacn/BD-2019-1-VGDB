from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo

# from ..models import Employee


class CreateReview(FlaskForm):
    """
    Form for create review
    """

    score = StringField('Name', validators=[DataRequired()])
    description = StringField('Name', validators=[DataRequired()])
    game_id = StringField('Name', validators=[DataRequired()])
    users_id = StringField('Name', validators=[DataRequired()])

    # email = StringField('Email', validators=[DataRequired(), Email()])
    # username = StringField('Username', validators=[DataRequired()])
    # first_name = StringField('First Name', validators=[DataRequired()])
    # last_name = StringField('Last Name', validators=[DataRequired()])
    # password = PasswordField('Password', validators=[
    #                                     DataRequired(),
    #                                     EqualTo('confirm_password')
    #                                     ])
    # confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Submit')

    # def validate_email(self, field):
    #     if Employee.query.filter_by(email=field.data).first():
    #         raise ValidationError('Email is already in use.')

    # def validate_username(self, field):
    #     if Employee.query.filter_by(username=field.data).first():
    #         raise ValidationError('Username is already in use.')
