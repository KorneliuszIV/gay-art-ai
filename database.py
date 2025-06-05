from flask import g 
import os
import sqlite3
import psycopg2

DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app.db")

def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(os.environ.get('DATABASE_URL'))
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()