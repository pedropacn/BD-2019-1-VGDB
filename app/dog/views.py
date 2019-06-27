from flask import flash, redirect, render_template, url_for
# from flask_login import login_required

from . import dog
from .forms import CreateDog
from ..database.dogs import Dogs


@dog.route('/dogs')
def index():
    """
    Render the index template
    """
    dogs = Dogs()
    print(dogs.all())
    return render_template('dog/index.html', title="Index", dogs=dogs.all())


@dog.route('/dogs/new', methods=['GET', 'POST'])
def new():
    """
    Render the new template
    """

    add_dog = True

    form = CreateDog()
    if form.validate_on_submit():

      try:
        dogo = {
          "name": form.name.data,
          "age": form.age.data
        }
        print(dogo)
        new_dog = Dogs()
        new_dog.create(**dogo)
        
        # add employee to the database
        flash('You have successfully created a Dog.')
      except:
        # in case department name already exists
        flash('Error: dog already exists.')
      

      # redirect to the login page
      return redirect(url_for('dog.index'))

    return render_template('dog/new.html', action="Add", add_dog=add_dog, form=form, title="Add Dog")

@dog.route("/dog/edit/<int:id>", methods=['GET', 'POST'])
def edit_dog(id):
    """
    Edit a dog
    """

    add_dog = False

    cur = Dogs()
    dog = cur.select(id)
    try:
      form = CreateDog(obj=dog)
    except:
      print("Cant find dog.")

    if form.validate_on_submit():
        dog["name"] = form.name.data
        dog["age"] = form.age.data
        cur.update(**dog)

        flash('You have successfully edited a dog.')

        # redirect to the departments page
        return redirect(url_for('dog.index'))
    
    form.age.data = dog["age"]
    form.name.data = dog["name"]
    return render_template('dog/new.html', action="Edit",
                           add_dog=add_dog, form=form,
                           dog=dog, title="Edit Dog")

@dog.route("/dog/delete/<int:id>", methods=['GET', 'POST'])
def delete_dog(id):
  """
    Delete a dog from the database
  """
  dog = Dogs()
  try:
    dog.delete(id)
    flash('You have successfully deleted the dog.')
  except:
    print("Cant delete dog.")

  # redirect to the departments page
  return redirect(url_for('dog.index'))

  return render_template(title="Delete Department")