#encoding: utf-8
import os

HOSTNAME = 'dpg-cngra2fsc6pc73b2sj90-a.singapore-postgres.render.com'
PORT     = '5432'
DATABASE = 'flask_cn45'
USERNAME = 'flask_cn45_user'
PASSWORD = 'RE1nMcdrvTma4tQwefeITrM6ZgbBDPxw'
DB_URI = 'postgresql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_ECHO = True

DEBUG = True

SECRET_KEY = 'course_management'