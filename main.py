import sqlite3
import os

from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv('DATABASE_URL')

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(DB_URL)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET'])
def root():
    return render_template('base.html')


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/users", methods=["GET"])  
def get_all_users():
    conn = get_db_connection()
    users_data = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template("users/list_users.html", users=users_data)


@app.route ('/users/create', methods= ['GET'])
def create_one_user():
    if request.method == "GET":
        return render_template('users/create.html')
   # if request.method == "POST":
   #     dni = request.form['dni']
   #     given_name = request.form['given_name']
   #     family_name = request.form['family_name']
   #     email = request.form['email']
   #     phone_number = request.form['phone_number']
#    direccion = request.form['direction']
        
   #     conn = get_db_connection()
   #    conn.execute('INSERT INTO users (dni, given_name, family_name, email, phone_number, direccion) VALUES (?, ?, ?, ?, ?, ?)', (dni, given_name, family_name, email, phone_number, direccion))
   #   conn.commit()
   #     conn.close()
   #     return redirect(url_for('get_all_users'))




