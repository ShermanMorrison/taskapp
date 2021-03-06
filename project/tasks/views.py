__author__ = 'jonathan'


#############
#  imports  #
#############

from functools import wraps
from flask import Flask, flash, redirect, render_template, \
    request, session, url_for, Blueprint

from .forms import AddTaskForm
from datetime import datetime
from project import db
from project.models import Task


##############
#   config   #
##############

tasks_blueprint = Blueprint('tasks', __name__)

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


def open_tasks():
    return db.session.query(Task).filter_by(
        status='1').order_by(Task.due_date.asc())


def closed_tasks():
    return db.session.query(Task).filter_by(
        status='0').order_by(Task.due_date.asc())


# route to display tasks
@tasks_blueprint.route('/tasks/')
@login_required
def tasks():
    return render_template(
        'tasks.html',
        form=AddTaskForm(request.form),
        open_tasks=open_tasks(),
        closed_tasks=closed_tasks()
    )

# Add new task
@tasks_blueprint.route('/add/', methods=['GET', 'POST'])
@login_required
def new_task():
    error = None
    form = AddTaskForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            task_to_add = Task(
                form.name.data,
                form.due_date.data,
                form.priority.data,
                datetime.utcnow(),
                '1',
                session['user_id']
            )
            db.session.add(task_to_add)
            db.session.commit()
            flash('New entry was successfully posted.')
            return redirect(url_for('tasks.tasks'))

    return render_template(url_for('tasks.tasks'), form=form, error=error, open_tasks=open_tasks(),
                           closed_tasks=closed_tasks())


# Mark task as complete, using dynamic routing
@tasks_blueprint.route('/complete/<int:task_id>/')
@login_required
def complete(task_id):
    db.session.query(Task) \
        .filter_by(task_id=task_id).update({"status": "0"})
    db.session.commit()
    flash('The task with id = ' + str(task_id) + ' was marked as complete')
    return redirect(url_for('tasks.tasks'))

# Delete task, using dynamic routing
@tasks_blueprint.route('/delete/<int:task_id>/')
@login_required
def delete_entry(task_id):
    db.session.query(Task) \
        .filter_by(task_id=task_id).delete()
    db.session.commit()
    flash('Deleted task with id = ' + str(task_id))
    return redirect(url_for('tasks.tasks'))

