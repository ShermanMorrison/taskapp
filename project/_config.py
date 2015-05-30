__author__ = 'jonathan'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'taskapp.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = '\x04\x875(\x932t\xc6+9uT!yQ\x8c\xba\xd2a\xe4\xee\xa4\xc9\x97'

DATABASE_PATH = os.path.join(basedir, DATABASE)

# print DATABASE
# print DATABASE_PATH
# print __file__