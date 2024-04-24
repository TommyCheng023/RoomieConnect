from flask import render_template, request, redirect, session, url_for, flash, abort
from config import Config
import mysql.connector
import bcrypt


def profile():
  """
  It takes the user's inputs, and rewrites it in the database.
  """
  
  db = mysql.connector.connect(
      host=Config.DATABASE_HOST,
      user=Config.DATABASE_USER,
      password=Config.DATABASE_PASSWORD,
      database=Config.DATABASE_DB
  )
  cur = db.cursor(buffered=True,dictionary=True)

  email = request.args.get('bu_email')

  cur.execute("SELECT * FROM User WHERE bu_email = (%s)", (email,))
  user_info = cur.fetchone()
  
   
  cur.close()
  db.close()
  

  return render_template("personal-profile-page.html", user_info=user_info)
