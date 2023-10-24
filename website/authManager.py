from flask import Blueprint,  render_template ,request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login/',methods=['GET','POST'])
def login():
    data = request.form 
    print(data)
    return render_template("login.html",boolean = True)

@auth.route('/logout/')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up/',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        email2 = request.form.get("email2")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        if len(email) < 4:
            flash('Email must be more than 4 characters!', category='error')
            pass
        elif email == email2:
            flash('backup email is the same as your main email!',category='warning')
            pass
        elif len(username)< 2:
            flash('Username must be more than 2 characters!', category='error')
            pass           
        elif password1 != password2:
            flash('Passowrds must match!', category='error')
            pass
          
        elif len(password1) < 7:
            flash('Password must be more than 7 characters!', category='error')
            pass
        else:
            data = request.form 
            print(data)
            flash('Account is being created!', category='success')
            return render_template("home.html")
        return render_template("sign_up.html")    
    else:
        return render_template("sign_up.html") 
    

@auth.route('/adminportal/')
def adminPortal():
    return render_template("adminportal.html") 

"""@auth.route('/log-admin')
def log_admin():
    return "<h1>log-admin</h1>"  
"""