from sqlalchemy import or_

from course import course_blue
from flask import Flask, render_template, request, flash, session, jsonify, redirect, url_for, abort
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired,EqualTo
from flask_sqlalchemy import SQLAlchemy
from models import User, Course
from models import db
import math


@course_blue.route('/index/<int:page>')
def index(page=1):
    try:
        offset = (page - 1) * 10
        courses = Course.query.offset(offset).limit(10).all()
        page_count = math.ceil(Course.query.count() / 10)
    except Exception as e:
        abort(404)


    return render_template('index.html', courses=courses, page=page, page_count=page_count)


@course_blue.route('/d/<id>/')
def detail(id):
    course = Course.query.get(id)
    return render_template('detail.html',course=course)

@course_blue.route('/search/')
def search():
    q = request.args.get('q')
    courses = Course.query.filter(or_(Course.course_title.contains(q), Course.modules.contains(q),
                                        Course.instructor.contains(q), Course.offered_by.contains(q),
                                        Course.keyword.contains(q)))

    return render_template('index.html', courses=courses)


@course_blue.route('/question/')
def question():
    return 'question'
    question_model = Course.query.get(id)
    return render_template('detail.html',question=question_model)