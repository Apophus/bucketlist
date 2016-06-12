#!usr/bin/python

import os
basedir =os.path.abspath(os.path.dirname(__file__))

#path to the databasefile
SAQALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#this is where SQLAlchemy-migrate data files are stored
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


