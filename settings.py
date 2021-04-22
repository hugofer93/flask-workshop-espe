import os

from decouple import config


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = config('SECRET_KEY')

ENV = config('FLASK_ENV', default='development')

DEBUG = config('FLASK_DEBUG', default=True, cast=bool)

DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')