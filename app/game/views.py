from flask import flash, redirect, render_template, url_for
# from flask_login import login_required

from . import game
from .forms import CreateGame
from ..database.games import Games


@game.route('/games')
def index():
    """
    Render the index template
    """
    games = Games()
    print(games.all())
    return render_template('game/index.html', title="Index", games=games.all())


@game.route('/games/new', methods=['GET', 'POST'])
def new():
    """
    Render the new template
    """

    add_game = True

    form = CreateGame()
    if form.validate_on_submit():

      try:
        game = {
            "name": form.name.data,
            "score_critics": float(form.score_critics.data),
            "genres_id": form.genres_id.data,
            "series_id": form.series_id.data
        }

        print(game)
        new_game = Games()
        new_game.create(**game)

        # add employee to the database
        flash('You have successfully created a Game.')
      except:
        # in case department name already exists
        flash('Error: game already exists.')

      # redirect to the login page
      return redirect(url_for('game.index'))

    return render_template('game/new.html', action="Add", add_game=add_game, form=form, title="Add Game")


@game.route("/game/edit/<int:id>", methods=['GET', 'POST'])
def edit_game(id):
    """
    Edit a game
    """

    add_game = False

    cur = Games()
    game = cur.select(id)
    try:
      form = CreateGame(obj=game)
    except:
      print("Cant find game.")

    if form.validate_on_submit():
        game["name"] = form.name.data
        game["score_critics"] = form.score_critics.data
        game["genres_id"] = form.genres_id.data
        game["series_id"] = form.series_id.data
        cur.update(**game)

        flash('You have successfully edited a game.')

        # redirect to the departments page
        return redirect(url_for('game.index'))

    form.name.data = game["name"]
    form.score_critics.data = game["score_critics"]
    form.genres_id.data = game["genres_id"]
    form.series_id.data = game["series_id"]
    
    return render_template('game/new.html', action="Edit",
                           add_game=add_game, form=form,
                           game=game, title="Edit Game")


@game.route("/game/delete/<int:id>", methods=['GET', 'POST'])
def delete_game(id):
  """
    Delete a game from the database
  """
  game = Games()
  try:
    game.delete(id)
    flash('You have successfully deleted the game.')
  except:
    print("Cant delete game.")

  # redirect to the departments page
  return redirect(url_for('game.index'))

  return render_template(title="Delete Department")
