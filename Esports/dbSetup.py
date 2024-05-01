import sqlite3

conn = sqlite3.connect('Esports.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE user (username TEXT UNIQUE, hashed_password TEXT, userid INTEGER PRIMARY KEY)
''')


cursor.execute('''
CREATE TABLE Teams (team_id INTEGER PRIMARY KEY, team_name TEXT, team_owner TEXT, 
team_members LIST, team_events DICT)
''')

cursor.execute('''
CREATE TABLE Events (EventID INTEGER PRIMARY KEY, EventName TEXT, EventGame TEXT UNIQUE)''')