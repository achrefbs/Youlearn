from app import db, app
from datetime import datetime



class Category(db.Model):
    __table_args__ = {'extend_existing': True}
    categoryid = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Category('{self.categoryid}', '{self.category_name}')"


class Course(db.Model):
    __table_args__ = {'extend_existing': True}
    courseid = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    regular_price = db.Column(db.DECIMAL)
    discounted_price = db.Column(db.DECIMAL)


    def __repr__(self):
        return f"Course('{self.courseid}','{self.course_name}','{self.description}', '{self.image}', '{self.regular_price}', '{self.discounted_price}')"


class CourseCategory(db.Model):
    __table_args__ = {'extend_existing': True}
    categoryid = db.Column(db.Integer, db.ForeignKey('category.categoryid'), nullable=False, primary_key=True)
    courseid = db.Column(db.Integer, db.ForeignKey('course.courseid'), nullable=False, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Product('{self.categoryid}', '{self.courseid}')"
