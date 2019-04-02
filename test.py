#-*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://postgres:2643383@localhost/proxyget')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://sabcdxxljcjdtn:864ba46dec25227bf55fe8ee1d72530adac212a6f1f13da1e0603f94bc2ea118@ec2-184-73-153-64.compute-1.amazonaws.com:5432/d3sfutm4pft2ed'#DATABASE_URL
db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = "answers"
	id = db.Column(db.Integer, primary_key=True)
	stu_id = db.Column(db.String(100))
	name = db.Column(db.String(100))
	passport = db.Column(db.String(100))
	nationality = db.Column(db.String(100))
	grade = db.Column(db.String(100))
	major = db.Column(db.String(100))
	remarks = db.Column(db.String(100))

	def __init__(self, stu_id, name, passport, nationality, grade, major, remarks):
		self.stu_id = stu_id
		self.name = name
		self.passport = passport
		self.nationality = nationality
		self.grade = grade
		self.major = major
		self.remarks = remarks

@app.route("/", methods=['GET'])
def mainpage():
	return render_template('q.html', data=User.query.all())

@app.route('/data', methods=['POST'])
def user():
	print ("insert now")
	u = User(request.form['stu_id'], request.form['name'], request.form['passport'], request.form['nationality'], request.form['grade'], request.form['major'], request.form['remarks'])
	db.session.add(u)
	db.session.commit()
	return redirect(url_for('mainpage'))

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)
