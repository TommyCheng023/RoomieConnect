from flask import request, redirect, url_for, render_template, flash, session
import mysql.connector
from config import Config
import bcrypt

def login():
    """
        It applies the login process, mainly to fetch and check if the user-input password is the same as the password stored in the database.
    """

    if request.method == 'POST':
        db = mysql.connector.connect(
            host=Config.DATABASE_HOST,
            user=Config.DATABASE_USER,
            password=Config.DATABASE_PASSWORD,
            database=Config.DATABASE_DB
        )

        cur = db.cursor(buffered=True)

        input_email = request.form['email']
        input_password = request.form['password']

        # try: fetch the user with the matched email from the database
        cur.execute('SELECT * FROM User WHERE bu_email = (%s)', (input_email,))
        user = cur.fetchone()
        if user:
            encoded_password = input_password.encode('utf-8')
            stored_password = user[1].encode('utf-8')
            if bcrypt.checkpw(encoded_password, stored_password):
                user_name = user[4]
                flash('Login successful. Welcome!')
                session['email'] = input_email
                session['name'] = user_name
                session.permanent = True     # monitor inactivity
                return redirect(url_for('home'))
            else:
                flash('Incorrect password! :(')
                return redirect(url_for('login'))
        else:
            flash('User does not exist.')
            return redirect(url_for('login'))
    
    return render_template('login_page.html')
        