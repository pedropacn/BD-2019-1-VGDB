from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo

# from ..models import Employee


class CreateReview(FlaskForm):
    """
    Form for create review
    """

    score = StringField('Score', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    game_id = StringField('Game', validators=[DataRequired()])
    users_id = StringField('User', validators=[DataRequired()])

    submit = SubmitField('Submit')