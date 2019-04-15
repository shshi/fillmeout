#-*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://postgres:2643383@localhost/proxyget')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://sabcdxxljcjdtn:864ba46dec25227bf55fe8ee1d72530adac212a6f1f13da1e0603f94bc2ea118@ec2-184-73-153-64.compute-1.amazonaws.com:5432/d3sfutm4pft2ed'#DATABASE_URL
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2643383@localhost/dlu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):
	#__tablename__ = "stu_info"
	id = db.Column(db.Integer, primary_key=True)
	idx = db.Column(db.String(100))
	stu_id = db.Column(db.String(100))
	app_no = db.Column(db.String(100))
	stu_no = db.Column(db.String(100))
	surname = db.Column(db.String(100))
	givenname = db.Column(db.String(100))
	fullname = db.Column(db.String(100))
	chinesename = db.Column(db.String(100))
	passport = db.Column(db.String(100))
	birthday = db.Column(db.String(100))
	nationality = db.Column(db.String(100))
	sex = db.Column(db.String(100))
	card_id = db.Column(db.String(100))

	degree_app = db.Column(db.String(100))
	birthplace = db.Column(db.String(100))
	faculty = db.Column(db.String(100))
	major = db.Column(db.String(100))
	length = db.Column(db.String(100))

	reg_fee = db.Column(db.String(100))
	tuition = db.Column(db.String(100))
	stu_type = db.Column(db.String(100))
	marry = db.Column(db.String(100))
	reg_year = db.Column(db.String(100))
	reg_season = db.Column(db.String(100))
	stu_status = db.Column(db.String(100))

	reason_leave = db.Column(db.String(100))
	time_start = db.Column(db.String(100))
	time_finish = db.Column(db.String(100))
	study_lan = db.Column(db.String(100))
	feefrom = db.Column(db.String(100))
	religion = db.Column(db.String(100))
	address = db.Column(db.String(100))

	tel = db.Column(db.String(100))
	email = db.Column(db.String(100))
	major_dir = db.Column(db.String(100))
	study_topic = db.Column(db.String(100))
	mentor = db.Column(db.String(100))
	stay = db.Column(db.String(100))
	scholarship = db.Column(db.String(100))

	short_team = db.Column(db.String(100))
	fee_method = db.Column(db.String(100))
	grade = db.Column(db.String(100))
	study_limit = db.Column(db.String(100))
	app_date = db.Column(db.String(100))
	admit_date = db.Column(db.String(100))
	reg_date = db.Column(db.String(100))

	grad_date = db.Column(db.String(100))
	leav_date = db.Column(db.String(100))
	leav_date_asm = db.Column(db.String(100))
	hsk_score = db.Column(db.String(100))
	college = db.Column(db.String(100))
	latest_degree = db.Column(db.String(100))
	occupation = db.Column(db.String(100))

	work_place = db.Column(db.String(100))
	ch_school = db.Column(db.String(100))
	ch_en_school = db.Column(db.String(100))
	ch_start = db.Column(db.String(100))
	ch_finish = db.Column(db.String(100))
	recomm_from = db.Column(db.String(100))
	recomm_tel = db.Column(db.String(100))

	trustee = db.Column(db.String(100))
	tel_trustee = db.Column(db.String(100))
	econ_trustee = db.Column(db.String(100))
	mother_lan = db.Column(db.String(100))
	goodat = db.Column(db.String(100))
	ch_lan = db.Column(db.String(100))
	en_lan = db.Column(db.String(100))

	other_lan = db.Column(db.String(100))
	guardian = db.Column(db.String(100))
	ch_family = db.Column(db.String(100))
	ch_tel = db.Column(db.String(100))
	addr_now = db.Column(db.String(100))
	en_dlu = db.Column(db.String(100))
	ch_dlu = db.Column(db.String(100))

	en_or = db.Column(db.String(100))
	reg_from = db.Column(db.String(100))
	reg_deadline = db.Column(db.String(100))
	visa_type = db.Column(db.String(100))
	visa_to = db.Column(db.String(100))
	stay_no = db.Column(db.String(100))
	stay_to = db.Column(db.String(100))

	remarks = db.Column(db.String(100))
	quane = db.Column(db.String(100))
	bufen_tuition = db.Column(db.String(100))
	bufen_accom = db.Column(db.String(100))
	bufen_med = db.Column(db.String(100))
	bufen_book = db.Column(db.String(100))
	qita = db.Column(db.String(100))

	fee_type = db.Column(db.String(100))
	fee_status = db.Column(db.String(100))
	fee_total = db.Column(db.String(100))
	class_name = db.Column(db.String(100))
	great_stu_type = db.Column(db.String(100))
	family_info = db.Column(db.String(100))
	history = db.Column(db.String(100))

	table_no = db.Column(db.String(100))
	country_send = db.Column(db.String(100))
	send_via = db.Column(db.String(100))


	def __init__(self, idx, stu_id, app_no, stu_no, surname, givenname, fullname, chinesename, passport, birthday, nationality, sex, card_id, degree_app, birthplace, faculty, major, length, reg_fee, tuition, stu_type, marry, reg_year, reg_season, stu_status, reason_leave, time_start, time_finish, study_lan, feefrom, religion, address, tel, email, major_dir, study_topic, mentor, stay, scholarship, short_team, fee_method, grade, study_limit, app_date, admit_date, reg_date, grad_date, leav_date, leav_date_asm, hsk_score, college, latest_degree, occupation, work_place, ch_school, ch_en_school, ch_start, ch_finish, recomm_from, recomm_tel, trustee, tel_trustee, econ_trustee, mother_lan, goodat, ch_lan, en_lan, other_lan, guardian, ch_family, ch_tel, addr_now, en_dlu, ch_dlu, en_or, reg_from, reg_deadline, visa_type, visa_to, stay_no, stay_to, remarks, quane, bufen_tuition, bufen_accom, bufen_med, bufen_book, qita, fee_type, fee_status, fee_total, class_name, great_stu_type, family_info, history, table_no, country_send, send_via):
		self.idx=idx
		self.stu_id=stu_id
		self.app_no=app_no
		self.stu_no=stu_no
		self.surname=surname
		self.givenname=givenname
		self.fullname=fullname
		self.chinesename=chinesename
		self.passport=passport
		self.birthday=birthday
		self.nationality=nationality
		self.sex=sex
		self.card_id=card_id
		self.degree_app=degree_app
		self.birthplace=birthplace
		self.faculty=faculty
		self.major=major
		self.length=length
		self.reg_fee=reg_fee
		self.tuition=tuition
		self.stu_type=stu_type
		self.marry=marry
		self.reg_year=reg_year
		self.reg_season=reg_season
		self.stu_status=stu_status
		self.reason_leave=reason_leave
		self.time_start=time_start
		self.time_finish=time_finish
		self.study_lan=study_lan
		self.feefrom=feefrom
		self.religion=religion
		self.address=address
		self.tel=tel
		self.email=email
		self.major_dir=major_dir
		self.study_topic=study_topic
		self.mentor=mentor
		self.stay=stay
		self.scholarship=scholarship
		self.short_team=short_team
		self.fee_method=fee_method
		self.grade=grade
		self.study_limit=study_limit
		self.app_date=app_date
		self.admit_date=admit_date
		self.reg_date=reg_date
		self.grad_date=grad_date
		self.leav_date=leav_date
		self.leav_date_asm=leav_date_asm
		self.hsk_score=hsk_score
		self.college=college
		self.latest_degree=latest_degree
		self.occupation=occupation
		self.work_place=work_place
		self.ch_school=ch_school
		self.ch_en_school=ch_en_school
		self.ch_start=ch_start
		self.ch_finish=ch_finish
		self.recomm_from=recomm_from
		self.recomm_tel=recomm_tel
		self.trustee=trustee
		self.tel_trustee=tel_trustee
		self.econ_trustee=econ_trustee
		self.mother_lan=mother_lan
		self.goodat=goodat
		self.ch_lan=ch_lan
		self.en_lan=en_lan
		self.other_lan=other_lan
		self.guardian=guardian
		self.ch_family=ch_family
		self.ch_tel=ch_tel
		self.addr_now=addr_now
		self.en_dlu=en_dlu
		self.ch_dlu=ch_dlu
		self.en_or=en_or
		self.reg_from=reg_from
		self.reg_deadline=reg_deadline
		self.visa_type=visa_type
		self.visa_to=visa_to
		self.stay_no=stay_no
		self.stay_to=stay_to
		self.remarks=remarks
		self.quane=quane
		self.bufen_tuition=bufen_tuition
		self.bufen_accom=bufen_accom
		self.bufen_med=bufen_med
		self.bufen_book=bufen_book
		self.qita=qita
		self.fee_type=fee_type
		self.fee_status=fee_status
		self.fee_total=fee_total
		self.class_name=class_name
		self.great_stu_type=great_stu_type
		self.family_info=family_info
		self.history=history
		self.table_no=table_no
		self.country_send=country_send
		self.send_via=send_via


@app.route("/", methods=['GET'])
def mainpage():
	return render_template('f.html', data=User.query.all())

@app.route('/submit', methods=['POST'])
def user():
	print ("insert now")
	u = User(request.form['idx'], request.form['stu_id'], request.form['app_no'], request.form['stu_no'], request.form['surname'], request.form['givenname'], request.form['fullname'], request.form['chinesename'], request.form['passport'], request.form['birthday'], request.form['nationality'], request.form['sex'], request.form['card_id'], request.form['degree_app'], request.form['birthplace'], request.form['faculty'], request.form['major'], request.form['length'], request.form['reg_fee'], request.form['tuition'], request.form['stu_type'], request.form['marry'], request.form['reg_year'], request.form['reg_season'], request.form['stu_status'], request.form['reason_leave'], request.form['time_start'], request.form['time_finish'], request.form['study_lan'], request.form['feefrom'], request.form['religion'], request.form['address'], request.form['tel'], request.form['email'], request.form['major_dir'], request.form['study_topic'], request.form['mentor'], request.form['stay'], request.form['scholarship'], request.form['short_team'], request.form['fee_method'], request.form['grade'], request.form['study_limit'], request.form['app_date'], request.form['admit_date'], request.form['reg_date'], request.form['grad_date'], request.form['leav_date'], request.form['leav_date_asm'], request.form['hsk_score'], request.form['college'], request.form['latest_degree'], request.form['occupation'], request.form['work_place'], request.form['ch_school'], request.form['ch_en_school'], request.form['ch_start'], request.form['ch_finish'], request.form['recomm_from'], request.form['recomm_tel'], request.form['trustee'], request.form['tel_trustee'], request.form['econ_trustee'], request.form['mother_lan'], request.form['goodat'], request.form['ch_lan'], request.form['en_lan'], request.form['other_lan'], request.form['guardian'], request.form['ch_family'], request.form['ch_tel'], request.form['addr_now'], request.form['en_dlu'], request.form['ch_dlu'], request.form['en_or'], request.form['reg_from'], request.form['reg_deadline'], request.form['visa_type'], request.form['visa_to'], request.form['stay_no'], request.form['stay_to'], request.form['remarks'], request.form['quane'], request.form['bufen_tuition'], request.form['bufen_accom'], request.form['bufen_med'], request.form['bufen_book'], request.form['qita'], request.form['fee_type'], request.form['fee_status'], request.form['fee_total'], request.form['class_name'], request.form['great_stu_type'], request.form['family_info'], request.form['history'], request.form['table_no'], request.form['country_send'], request.form['send_via'])
	db.session.add(u)
	db.session.commit()
	#return redirect(url_for('mainpage'))
	return '提交成功'

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)
