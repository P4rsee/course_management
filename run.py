from flask import Flask, redirect, url_for, session, g
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, add_course, add_insititution, add_data
import config
from user import user_blue
from course import course_blue


def create_app():
    app1 = Flask(__name__)

    app1.config.from_object(config)

    app1.register_blueprint(user_blue)
    app1.register_blueprint(course_blue)

    db.init_app(app1)
    return app1


app = create_app()