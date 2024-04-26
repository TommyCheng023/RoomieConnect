from flask import render_template, session
from config import Config
import mysql.connector

def edit():
    """
        Generate an edit template for the profile page.
    """
    db = mysql.connector.connect(
        host=Config.DATABASE_HOST,
        user=Config.DATABASE_USER,
        password=Config.DATABASE_PASSWORD,
        database=Config.DATABASE_DB
    )
    cur = db.cursor(buffered=True,dictionary=True)

    email = session.get('email')

    cur.execute("SELECT * FROM User WHERE bu_email = (%s)", (email,))
    user_info = cur.fetchone()
    
    
    cur.close()
    db.close()
    return render_template('personal_profile_page.html', info=user_info, editable=True)