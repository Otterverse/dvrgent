import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
SQLALCHEMY_DATABASE_URI = 'sqlite:///../dvrgent.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False