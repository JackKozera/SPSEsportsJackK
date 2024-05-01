from flask import Flask, render_template, g, request, redirect, url_for, session
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = 'theSecret'

@app.route('/', methods=['GET', 'POST'])
def index():
    print(session)
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_check = request.form.get('password_check')
        if password == password_check:
            password = bcrypt.hashpw(password.encode('utf-8'))
            try:
                with sqlite3.connect('Esports.db') as db:
                    cursor = db.cursor()
                    cursor.execute('''INSERT INTO user (username, saved_password) VALUES (?, ?)''', (username, password))
                    db.commit()
                    print("registered successfully")
                    return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                print("username already exists")
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(session)
    return render_template('login.html')

@app.route('/search')
def search():
    return render_template('search.html')
        
if __name__ == '__main__':
    app.run(debug=True)