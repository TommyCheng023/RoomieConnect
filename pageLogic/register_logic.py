from flask import render_template, request, redirect, session, url_for, flash, abort
import config

def register():
    """
        It applies validation testing on user's inputs and submit them to the database to complete registration,
        or it shows up the registration page to the user.
    """

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        verify_password = request.form['verify-password']
        real_name = request.form['real-name']
        gender = request.form['gender']
        grade = request.form['classification']
        age = request.form['age']
        pref = request.form['building-pref']
        budget = request.form['budget']
        user = False # dummy for testing
        domain = "bu.edu" # dummy for testing
        
        # mydb = config.mydb()
        # cur = mydb.cursor(buffered=True, dictionary=True)
        # cur.execute('SELECT * FROM users WHERE email = (%s)', (email,))
        # user = cur.fetchone()
        # usename, domain = email.split("@")

        if user:
            flash('Email already registered!', category='error')
            return redirect(url_for('register'))
        elif len(email) < 4:
            flash('Incorrect email format!', category='error')
            return redirect(url_for('register'))
        elif "@" not in email:
            flash('Incorrect email format!', category='error')
            return redirect(url_for('register'))
        elif domain != "bu.edu":
            flash('Please use a BU email!', category='error')
            return redirect(url_for('register'))
        elif password != verify_password:
            flash('Verified password not align with the first one.', category='error')
            return redirect(url_for('register'))
        elif len(password) < 8:
            flash('Password needs no less than 8 characters.', category='error')
            return redirect(url_for('register'))
        elif len(password) > 20:
            flash('Password needs no more than 20 characters.', category='error')
            return redirect(url_for('register'))
        elif any(char in password for char in ['{', '}', '[', ']', '(', ')', ';', "'", '"', '=', '<', '>', '#', '%', '&', '|', '`']):  #这些符号在读取时可能会导致程序错误
            flash('Invalid characters detected: {, }, [, ], (, ), ;, "'", '" ', =, <, >, #, %, &, |, `.', category='error')
            return redirect(url_for('register'))
        else:
            flash('Dummy Message: success')
            
    return render_template("registration_page.html")