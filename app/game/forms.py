from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField, DecimalField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired

# from ..models import Employee
from ..database.genres import Genres
from ..database.series import Series

class CreateGame(FlaskForm):
    """
    Form for create game
    """
    # form
    genres = Genres()
    series = Series()

    name = StringField('Name', validators=[DataRequired()])
    score_critics = DecimalField('Score', validators=[DataRequired()])
    genres_id = SelectField('Genre', choices=[(genre['id'], genre['name']) for genre in genres.all()], validators=[DataRequired()], coerce=int)
    series_id = SelectField('Series', choices=[(serie['id'], serie['name']) for serie in series.all()], coerce=int)
    # art = FileField('Image File', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])

    submit = SubmitField('Submit')
