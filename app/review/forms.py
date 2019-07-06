from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField, SelectField, DecimalField
from wtforms.validators import DataRequired, Email, EqualTo

# from ..models import Employee

from ..database.games import Games
from app.models import User

class CreateReview(FlaskForm):
    """
    Form for create review
    """

    users = User()
    games = Games()

    score = DecimalField('Score', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    game_id = SelectField('Game', choices=[(game['id'], game['name']) for game in games.all()], validators=[DataRequired()], coerce=int)
    users_id = SelectField('User', choices=[(user['id'], user['first_name']) for user in users.all()], validators=[DataRequired()], coerce=int)

    submit = SubmitField('Submit')