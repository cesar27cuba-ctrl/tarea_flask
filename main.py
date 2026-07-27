import sqlite3
import os

from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv('DATABASE_URL')

app = Flask(__name__)

def get_db():
    db = sqlite3.connect(DB_URL)
    db.row_factory = sqlite3.Row
    return db


@app.route('/', methods=['GET'])
def home():
    return render_template('base.html')


@app.route('/texto', methods=['GET'])
def text():
    return "hola con todos"


@app.route('/user', methods=['GET'])
def list_users():
    connection = get_db()
    users_data = connection.execute("SELECT * FROM users").fetchall()
    connection.close()
    return render_template('index.html', users_list=users_data)


@app.route('/api/users', methods=['GET'])
def list_users_json():
    connection = get_db()
    users_data = connection.execute("SELECT * FROM users").fetchall()
    connection.close()
    return jsonify(users_data)


