from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note, User, Portfolio 


from . import db
import json

views = Blueprint("views", __name__)
public = Blueprint("public",__name__, template_folder='/public/')


@views.route('/home/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html",user=current_user)


@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/portfolio/', methods=['GET', 'POST'])
@login_required
def portfolio():
    
    return render_template("portfolio.html", user=current_user)

@views.route('/settings/', methods=['GET', 'POST'])
@login_required
def settings():
    
    return render_template("settings.html", user=current_user)
    
@views.route("/")
def welcome():
    userDetails=current_user
    flash(f'Welcome {userDetails}')
    return render_template("welcome.html", user=current_user)

@public.route("/calculator/", methods=['GET', 'POST'])
def calculator():
    data = request.form
    print(data)
    return render_template("calculator.html",user=current_user)

@public.route("/support/", methods=['GET', 'POST'])
def welcome():
    return render_template("support.html",user=current_user)

@public.route("/about/", methods=['GET', 'POST'])
def about():
    data = request.form
    print(data)
    return render_template("about.html",user=current_user)


