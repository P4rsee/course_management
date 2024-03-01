from flask import Blueprint

course_blue = Blueprint('course', __name__, url_prefix='/course')
from . import views