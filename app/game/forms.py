from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField, DecimalField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

# from ..models import Employee

class CreateGame(FlaskForm):
    """
    Form for create game
    """

    name = StringField('Name', validators=[DataRequired()])
    score_critics = DecimalField('Score', validators=[DataRequired()])
    genres_id = SelectField('Genre', choices=[(1, 'Plataforma'), (2, 'Terror')], validators=[DataRequired()])
    series_id = SelectField('Series', choices=[(1, 'Mario'), (2, 'Silent Hill')])
