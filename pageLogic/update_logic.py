from flask import session, redirect, url_for, request, flash
from config import Config
import mysql.connector

def update():
    """
        Submit what the user has edited to the database. 
    """
    if request.method == 'POST':
        db = mysql.connector.connect(
            host=Config.DATABASE_HOST,
            user=Config.DATABASE_USER,
            password=Config.DATABASE_PASSWORD,
            database=Config.DATABASE_DB
        )
        cur = db.cursor(buffered=True,dictionary=True)
        email = session.get('email')
        email2 = request.form['email']
        if email != email2:
            # normally this case should never happen
            flash('Session mismatches your profile email, forced signing out.', 'error')
            session.clear()
            return redirect(url_for('login'))
        
        fullName = request.form['full-name']
        age = int(request.form['age'])
        classify = request.form['classification']
        pref1 = request.form['pref-1']
        pref2 = request.form['pref-2']
        pref3 = request.form['pref-3']
        budget = int(request.form['rent-budget'])
        intro = request.form['intro']
        exp = request.form['expect']
        status = int(request.form['status'])
        updated_data = {
            'bu_email': email2,
            'self_description': intro,
            'roommate_expectation': exp,
            'name': fullName,
            'academic_classification': classify,
            'age': age, 
            'building_preference1': pref1,
            'building_preference2': pref2,
            'building_preference3': pref3,
            'rent_budget': budget,
            'found_roommate': status
        }
        cur.execute('SELECT bu_email, self_description, roommate_expectation, name, academic_classification, age, building_preference1, building_preference2, building_preference3, rent_budget, found_roommate FROM User WHERE bu_email = (%s)', (email,))
        old_data = cur.fetchone()
        changes = {key: updated_data[key] for key in updated_data if str(updated_data[key]) != str(old_data[key])}
        cur.close()
        if changes:
            if age > 50 or age < 0:
                flash('Invalid age for this website.', 'error')
                return redirect(url_for('update'))
            query = """
                        UPDATE User SET
                        bu_email = %s, name = %s, age = %s, academic_classification = %s,
                        building_preference1 = %s, building_preference2 = %s, building_preference3 = %s, rent_budget = %s,
                        self_description = %s, roommate_expectation = %s, found_roommate = %s
                        WHERE bu_email = %s
                    """
            values = (
                updated_data['bu_email'], updated_data['name'], updated_data['age'],
                updated_data['academic_classification'], updated_data['building_preference1'], updated_data['building_preference2'],
                updated_data['building_preference3'], updated_data['rent_budget'], updated_data['self_description'],
                updated_data['roommate_expectation'], updated_data['found_roommate'], email2
            )
            cur = db.cursor(buffered=True,dictionary=True)   # reopen a cursor, just in case :3
            cur.execute(query, values)
            db.commit()
            cur.close()
            db.close()
            flash('Your profile is updated!', 'info')
            return redirect(url_for('profile'))

        else:
            flash('You did not make any changes!', 'error')
            return redirect(url_for('update'))
    

    return redirect(url_for('profile'))





