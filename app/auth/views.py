from flask import flash, redirect, render_template, url_for, session
from flask_login import login_required, login_user, logout_user, current_user

from . import auth
from .forms import LoginForm, RegistrationForm, ProfileForm

from app.models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """

    profile = False

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()

        new_user = {
            "email":form.email.data,
            "username":form.username.data,
            "first_name":form.first_name.data,
            "last_name":form.last_name.data,
            "password": user.password_hash(form.password.data)
                }

        # add user to the database
        user.create(**new_user)
        
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        cur = User()
        user = cur.filter_by(email=form.email.data)
        # print(user)
        # print(cur.verify_password(user['password'], form.password.data))
        if user is not None and cur.verify_password(user['password'], form.password.data):
            # log employee in
            login_user(cur)

            # redirect to the dashboard page after login
            return redirect(url_for('dog.index'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))

@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    profile = True

    cur = User()
    user = cur.select(current_user.id)
    user['password'] = ''
    try:
        form = ProfileForm(obj=user)
    except:
        print('cant find user.')

    if form.validate_on_submit():
        user["email"] = form.email.data
        user["username"] = form.username.data
        user["first_name"] = form.first_name.data
        user["last_name"] = form.last_name.data
        user["password"] =  cur.password_hash(form.password.data)
        cur.update(**user)

        flash('You have successfully edited the profile.')

        # redirect to the departments page
        return redirect(url_for('dog.index'))
    
    form.email.data = user["email"]
    form.username.data = user["username"]
    form.first_name.data = user["first_name"]
    form.last_name.data = user["last_name"]

    return render_template('auth/register.html', action="Edit",
    profile=profile, form=form,
    user=user, title="Profile")