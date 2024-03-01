from flask import Flask, redirect, url_for, session, g
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, add_course, add_insititution, add_data
import config
from user import user_blue
from course import course_blue


app = Flask(__name__)

app.config.from_object(config)

app.register_blueprint(user_blue)
app.register_blueprint(course_blue)

db.init_app(app)



## for base.html
@app.context_processor
def context_processor():
    if session.get('user_id'):
        return {"user": session['username']}
    else:
        return {}


## Login is required to access website data
@app.before_request
def require_login():
    allowed_routes = ['user.login', 'user.register', 'static']
    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect(url_for('user.login'))

@app.errorhandler(404)
def page_not_found(e):
    return 'Url is error. The homepage is /course/index/1'

@app.route('/',methods=['GET'])
def hello():
    return redirect(url_for('user.login'))


# with app.app_context():
#     db.drop_all()
#     db.create_all()
#     add_data()


if __name__ == '__main__':
    app.run()
