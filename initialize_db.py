import mysql.connector
from mysql.connector import errorcode

def create_database(cursor, database_name):
    try:
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {database_name} DEFAULT CHARACTER SET 'utf8';"
        )
        print(f"Database {database_name} created or already exists.")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)

def execute_sql_file(file_path, db):
    try:
        cursor = db.cursor()
        print(f"Executing script {file_path}...")
        with open(file_path, 'r') as file:
            sql_script = file.read()
        commands = sql_script.split(';')
        for command in commands:
            if command.strip():
                cursor.execute(command)
        cursor.close()
        db.commit()
        print("SQL script executed successfully.")
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")

if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': ''
    }
    database_name = 'RoomieConnect'
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        create_database(cursor, database_name)
        db.database = database_name  # Switch to the newly created database
        execute_sql_file('create.sql', db)
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")
    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print("MySQL connection is closed.")