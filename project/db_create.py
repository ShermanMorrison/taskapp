__author__ = 'jonathan'

from views import db
from models import Task
from datetime import date

# creates the tables imported above that extend db.Model
db.create_all()

#insert data into tasks table
db.session.add(Task("Finish the Task App", date(2015, 5, 31), 10, 1))
db.session.add(Task("Complete Django Tutorial", date(2015, 6, 1), 10, 1))

db.session.commit()
