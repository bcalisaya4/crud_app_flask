from flask import Flask, render_template, request, redirect, url_for,flash
import psycopg2

app = Flask(__name__)
# Postgres Connection
conn = psycopg2.connect(
        host="localhost",
        database="app_flask_db",
        user="postgres",
        password="root")

app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html',contacts = data)
    
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = conn.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s) ',
        (fullname,phone,email))
        conn.commit()
        flash("Saludo familia. Se a ingresado un usuario")
    return redirect(url_for('Index'))
        
@app.route('/edit')
def edit_contact():
    return 'Edit Contact'
        
@app.route('/delete')
def delete_contact():
    return 'Delete Contact'
    
if __name__ == '__main__':
    app.run(port = 3000, debug = True)