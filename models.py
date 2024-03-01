from flask_sqlalchemy import SQLAlchemy
import csv

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True)
    password = db.Column(db.String(32))

    def __repr__(self):
        return '<User: %s %s %s>' % (self.username, self.id, self.password)


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    course_title = db.Column(db.String(255))
    rating = db.Column(db.String(255))
    level = db.Column(db.String(255))
    schedule = db.Column(db.String(255))
    what_you_will_learn = db.Column(db.Text)
    skill_gain = db.Column(db.Text)
    modules = db.Column(db.Text)
    instructor = db.Column(db.Text)
    offered_by = db.Column(db.String(255), db.ForeignKey('institution.institution_name'))
    keyword = db.Column(db.String(255))
    course_url = db.Column(db.String(255))
    duration_to_complete = db.Column(db.String(255))
    number_of_review = db.Column(db.String(255))


class Institution(db.Model):
    __tablename__ = "institution"
    id = db.Column(db.Integer, autoincrement=True)
    institution_name = db.Column(db.String(255),primary_key=True)


course_file_name = './data/CourseraDataset-Clean.csv'
institution_file_name = './data/institution.csv'



def add_course():
    with open(course_file_name,"r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            for i in range(len(row)):
                row[i] = row[i].strip()
            course = Course(course_title=row[0], rating=row[1], level=row[2], schedule=row[3], what_you_will_learn=row[4],
                            skill_gain=row[5], modules=row[6], instructor=row[7],offered_by=row[8],keyword=row[9],course_url=row[10],
                            duration_to_complete=row[11],number_of_review=row[12])
            db.session.add(course)
        db.session.commit()
    return "add success"


def add_insititution():
    with open(institution_file_name,"r") as file:
        reader = csv.reader(file)
        next(reader)
        count = 1
        for row in reader:
            for i in range(len(row)):
                row[i] = row[i].strip()
            instituion = Institution(institution_name=row[0],id=count)
            count += 1
            db.session.add(instituion)
        db.session.commit()
    return "add success"



def add_data():
    add_insititution()
    add_course()




