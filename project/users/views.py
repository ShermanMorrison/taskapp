__author__ = 'jonathan'

#############
#  imports  #
#############

from functools import wraps
from flask import flash, redirect, render_template, \
    request, session, url_for, Blueprint
from sqlalchemy.exc import IntegrityError

from .forms import RegisterForm, LoginForm
from project import db
from project.models import User


##############
#   config   #
##############

users_blueprint = Blueprint('users', __name__)

#######################
#   helper functions  #
#######################

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You must log in to view this page')
            return redirect(url_for('users.login'))
    return wrap

#############
#   routes  #
#############


@users_blueprint.route('/logout/')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('Goodbye!')
    return redirect(url_for('users.login'))

@users_blueprint.route('/', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = db.session.query(User) \
                .filter_by(name=form.name.data).first()
            if user is not None and user.password == \
                    form.password.data:
                session['logged_in'] = True
                session['user_id'] = user.id
                flash('Welcome ' + user.name + "!")
                return redirect(url_for('tasks.tasks'))
            else:
                error = 'Invalid username or password.'
        else:
            error = 'Both fields are required'
    return render_template('login.html', form=form, error=error)


# register page.
# add to User table on POST
# render on GET
@users_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(
                form.name.data,
                form.email.data,
                form.password.data
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Thanks for registering. Please log in.')
                return redirect(url_for('users.login'))
            except IntegrityError:
                error = 'That username and/or email already exists.'
                return render_template('register.html', form=form, error=error)
    return render_template('register.html', form=form, error=error)


















