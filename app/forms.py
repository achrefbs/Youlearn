from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, SelectMultipleField, TextAreaField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from app import images

class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name')
    lastname = StringField('LastName')
    telephone = IntegerField('Telephone Number')
    profession = StringField('Profession')
    submit = SubmitField('Sign Up')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')



class addCategoryForm(FlaskForm):
    category_name = StringField('Category Name', validators=[DataRequired()])
    image = FileField('image')
    submit = SubmitField('Save')



class addCourseForm(FlaskForm):
    category = SelectField('Category:', coerce=int, id='select_category')
    CourseName = StringField('Course Name:', validators=[DataRequired()])
    CourseDescription = TextAreaField('Course Description:', validators=[DataRequired()])
    CoursePrice = FloatField('Course Price:', validators=[DataRequired()])
    image = FileField('image')
    submit = SubmitField('Save')