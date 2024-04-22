from flask import render_template
from config import Config
import mysql.connector

def showRoommates():
    """
        List all roommates' related information if they don't have a roommate yet.
    """
    db = mysql.connector.connect(
        host=Config.DATABASE_HOST,
        user=Config.DATABASE_USER,
        password=Config.DATABASE_PASSWORD,
        database=Config.DATABASE_DB
    )
    cur = db.cursor(dictionary=True, buffered=True)
    cur.execute('SELECT * FROM User WHERE found_roommate = %s LIMIT 10', (0,))
    profiles = cur.fetchall()
    cur.close()
    db.close()
    return render_template("roommates.html", profiles=profiles)