from flask import Blueprint, render_template, request

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")


@views.route('/calculator/')
def calculator():
    data = request.form 
    print(data)
    return render_template("calculator.html")



@views.route('/about/')
def about():
    data = request.form 
    print(data)
    return render_template("about.html")
