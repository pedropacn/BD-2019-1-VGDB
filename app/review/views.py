from flask import flash, redirect, render_template, url_for
# from flask_login import login_required

from . import review
from .forms import CreateReview
from ..database.reviews import Reviews


@review.route('/reviews')
def index():
    """
    Render the index template
    """
    reviews = Reviews()
    print(reviews.all())
    return render_template('review/index.html', title="Index", reviews=reviews.all())


@review.route('/reviews/new', methods=['GET', 'POST'])
def new():
    """
    Render the new template
    """

    add_review = True

    form = CreateReview()
    if form.validate_on_submit():

      try:
        review = {
          "score": float(form.score.data),
          "description": form.description.data,
          "games_id": form.game_id.data,
          "users_id": form.users_id.data
        }

        print(review)
        new_review = Reviews()
        new_review.create(**review)
        
        # add employee to the database
        flash('You have successfully created a Review.')
      except:
        # in case department name already exists
        flash('Error: review already exists.')
      

      # redirect to the login page
      return redirect(url_for('review.index'))

    return render_template('review/new.html', action="Add", add_review=add_review, form=form, title="Add Review")

@review.route("/review/edit/<int:id>", methods=['GET', 'POST'])
def edit_review(id):
    """
    Edit a review
    """

    add_review = False

    cur = Reviews()
    review = cur.select(id)
    try:
      form = CreateReview(obj=review)
    except:
      print("Cant find review.")

    if form.validate_on_submit():
        review["score"] = float(form.score.data)
        review["description"] = form.description.data
        review["games_id"] = form.game_id.data
        review["users_id"] = form.users_id.data
        cur.update(**review)

        flash('You have successfully edited a review.')

        # redirect to the departments page
        return redirect(url_for('review.index'))
    
    form.score.data = review["score"]
    form.description.data = review["description"]
    form.game_id.data = review["games_id"]
    form.users_id.data = review["users_id"]
    return render_template('review/new.html', action="Edit",
                           add_review=add_review, form=form,
                           review=review, title="Edit Review")

@review.route("/review/delete/<int:id>", methods=['GET', 'POST'])
def delete_review(id):
  """
    Delete a review from the database
  """
  review = Reviews()
  try:
    review.delete(id)
    flash('You have successfully deleted the review.')
  except:
    print("Cant delete review.")

  # redirect to the departments page
  return redirect(url_for('review.index'))

  return render_template(title="Delete Department")