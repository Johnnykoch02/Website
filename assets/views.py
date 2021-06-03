from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import Group, Note
from . import db
import json
import phonenumbers as pn


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        new_note = Note(text=note, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('New Note Added!', category="success")
        return redirect(url_for('views.home'))
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})

@views.route('/rentals-form', methods=['GET', 'POST'])
def rentals_form():
   # (user_id, full_name, phone_number, drivers_license, email_address, time_started, consent, active)
    if request.method == 'POST':
        fullName= request.form.get('full-name')
        signature = request.form.get('signature')
        licenseNumber = request.form.get('license-number')
        phoneNumber = request.form.get('phone-number')
        phoneNumber = pn.format_number(pn.parse(phoneNumber, 'US'), pn.PhoneNumberFormat.NATIONAL)
        emailAddress = request.form.get('email-address')
        new_group = Group(user_id=current_user.id, full_name=fullName, phone_number=phoneNumber, drivers_license=licenseNumber, email_address=emailAddress, consent=signature, active=True)
        db.session.add(new_group)
        db.session.commit()
        return redirect(url_for('views.rentals'))
    return render_template('rentals-form.html', user=current_user)
@views.route('/rentals', methods=['GET','POST'])
def rentals():
    return render_template('rentals.html', user=current_user)

@views.route('/unactivate-group', methods=['POST'])
def unactivate_group():
    group = json.loads(request.data)
    group_id = group['groupId']
    group = Group.query.get(group_id)
    print("in unactivate")
    if group:
        print("unactivating")
        if group.user_id == current_user.id:
            group.active = False
            db.session.commit()
    
    return jsonify({})

@views.route('/group-data-hecksher', methods=['GET'])
def group_data():
    return render_template('group-data-hecksher.html', user=current_user)


# user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     group_id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(72), unique=False)
#     last_name = db.Column(db.String(72), unique=False)
#     phone_number = db.Column(db.String(15), unique=False)
#     drivers_license = db.Column(db.String(20), unique=False)
#     email_address = db.Column(db.String(72), unique=False)
#     time_started = db.Column(db.DateTime(timezone=True), default=func.now())
#     consent = db.Column(db.String(72), unique=False)
#     active = db.Column(db.Boolean)