from flask import render_template, request, redirect, session, url_for, flash, abort
from config import Config
import mysql.connector
import bcrypt

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
        age = int(request.form['age'])
        pref = request.form['building-pref']
        pref_2 = request.form['building-pref-2']
        pref_3 = request.form['building-pref-3']
        budget = int(request.form['budget'])
        mate_exep = request.form['expectation']
        intro = request.form['self-intro']
        
        db = mysql.connector.connect(
            host=Config.DATABASE_HOST,
            user=Config.DATABASE_USER,
            password=Config.DATABASE_PASSWORD,
            database=Config.DATABASE_DB
        )

        cur = db.cursor(buffered=True, dictionary=True)
        cur.execute('SELECT * FROM User WHERE bu_email = (%s)', (email,))
        user = cur.fetchone()
        usename, domain = email.split("@")

        if user:
            flash('Email already registered! Please sign in.', 'error')
            return redirect(url_for('register'))
        elif len(email) < 4:
            flash('Incorrect email format!', 'error')
            return redirect(url_for('register'))
        elif "@" not in email:
            flash('Incorrect email format!', 'error')
            return redirect(url_for('register'))
        elif domain != "bu.edu":
            flash('Please use a BU email!', 'error')
            return redirect(url_for('register'))
        elif password != verify_password:
            flash('Verified password not align with the first one.', 'error')
            return redirect(url_for('register'))
        elif age > 50 or age < 0:
            flash('Invalid age for this website.', 'error')
            return redirect(url_for('register'))
        elif len(password) < 8:
            flash('Password needs no less than 8 characters.', 'error')
            return redirect(url_for('register'))
        elif len(password) > 20:
            flash('Password needs no more than 20 characters.', 'error')
            return redirect(url_for('register'))
        elif any(char in password for char in ['{', '}', '[', ']', '(', ')', ';', "'", '"', '=', '<', '>', '#', '%', '&', '|', '`']):  
            flash('Invalid characters detected: {, }, [, ], (, ), ;, "'", '" ', =, <, >, #, %, &, |, `.', 'error')
            return redirect(url_for('register'))
        else:
            # encode password
            password_bytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password_bytes, salt)

            # upload user information into the database
            cur.execute('INSERT INTO User VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (email, hashed_password, intro, mate_exep, real_name, gender, grade, age, pref, pref_2, pref_3, budget))
            db.commit()
            cur.close()
            db.close()

            flash('Successfully registered! You can login now.', 'info')
            return redirect(url_for('home'))
            
    return render_template("registration_page.html")