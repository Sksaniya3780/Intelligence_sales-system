import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_PATH = os.path.join(
    BASE_DIR,
    "sales.db"
)

def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn