__author__ = 'jonathan'

from views import db


class Task(db.Model):

    # assign hidden variable tablename
    __tablename__ = "tasks"

    # assign entries in each table row
    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer)

    # Constructor for table row
    def __init__(self, name, due_date, priority, status):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.status = status

    # magic method for string representing row
    def __repr__(self):
        return "<name {0}>".format(self.name)

