from app import app, db, images
from flask import Flask, render_template, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user
from app.forms import addCategoryForm, addCourseForm
from app.models.course import Category, Course, CourseCategory
import secrets
import os


@app.route('/')
@app.route('/home')
def index():
	courses = db.session.query(Course).all()
	count = db.session.query(Course).count()
	return render_template('index.html', title='YouLearn', courses=courses, count=count)

@app.route('/settings')
def settings():
	profile = {'email':current_user.email,'name':current_user.name, 'lastname':current_user.lastname, 'telephone': current_user.telephone}
	return render_template('settings.html', title='Settings', profile=profile)


@app.route('/profile')
@login_required
def profile():
	profile = {'email':current_user.email,'name':current_user.name, 'lastname':current_user.lastname, 'telephone': current_user.telephone}
	return render_template('profile.html', title='Profile', profile=profile)



@app.route("/admin/categories/new", methods=['GET', 'POST'])
def addCategory():
	
	form = addCategoryForm()
	if form.validate_on_submit():
		image = images.save(form.image.data)
		category = Category(category_name=form.category_name.data, image=image)
		db.session.add(category)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("addCategory.html", form=form)
	return redirect(url_for('index'))


@app.route("/admin/courses/new", methods=['GET', 'POST'])
def addCourse():
	form = addCourseForm()
	form.category.choices = [(row.categoryid, row.category_name) for row in Category.query.all()]
	if form.validate_on_submit():
		image = images.save(form.image.data)
		course = Course(course_name=form.CourseName.data, description=form.CourseDescription.data, discounted_price=15, regular_price=form.CoursePrice.data, image=image)
		db.session.add(course)
		db.session.commit()
		course_category = CourseCategory(categoryid=form.category.data, courseid=course.courseid)
		db.session.add(course_category)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("addCourse.html", form=form, legend="New Course")


@app.route("/course/<int:course_id>", methods=['GET'])
def course(course_id):
	course = Course.query.get_or_404(course_id)
	return render_template('Course.html', course=course)

def massageItemData(data):
	ans = []
	i = 0
	while i < len(data):
		curr = []
		for j in range(6):
			if i >= len(data):
				break
			curr.append(data[i])
			i += 1
		ans.append(curr)
	return ans

@app.route("/displayCategory/<int:categoryId>")
def displayCategory(categoryId):
	courseDetailsByCategoryId = Course.query.join(CourseCategory, Course.courseid == CourseCategory.courseid) \
		.add_columns(Course.courseid, Course.course_name, Course.regular_price, Course.discounted_price, Course.image
					 ) \
		.join(Category, Category.categoryid == CourseCategory.categoryid) \
		.filter(Category.categoryid == int(categoryId)) \
		.add_columns(Category.category_name) \
		.all()
	try:
		categoryName = courseDetailsByCategoryId[0].category_name
	except :
		categoryName = ""
	data = massageItemData(courseDetailsByCategoryId)
	if len(data) == 0:
		count = 0
	else :
		count = 1
	return render_template('displayCategory.html', data=data, categoryName=categoryName, count=count)


@app.route("/categories")
def categories():
	categories = db.session.query(Category).all()
	count = db.session.query(Category).count()
	return render_template('categories.html', categories=categories, count=count)

@app.route("/courses")
def displaycourses():
	courses = db.session.query(Course).all()
	count = db.session.query(Course).count()
	return render_template('courses.html', courses=courses, count=count)





@app.route("/courses/new", methods=['GET', 'POST'])
def NewCourse():
	form = addCourseForm()
	form.category.choices = [(row.categoryid, row.category_name) for row in Category.query.all()]
	if form.validate_on_submit():
		image = images.save(form.image.data)
		course = Course(course_name=form.CourseName.data, description=form.CourseDescription.data, discounted_price=15, regular_price=form.CoursePrice.data, image=image)
		db.session.add(course)
		db.session.commit()
		course_category = CourseCategory(categoryid=form.category.data, courseid=course.courseid)
		db.session.add(course_category)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("addCourse.html", form=form, legend="New Course")