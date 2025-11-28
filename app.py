from flask import Flask
import os
import pyodbc

app = Flask(__name__)

def get_db_connection2():
    conn_str = "DRIVER={ODBC Driver 18 for SQL Server};Server=tcp:owch-sql-server-pc38.database.windows.net,1433;Initial Catalog=flask-db;Persist Security Info=False;UID=sqladmin;Password=Felgi123lol1000;MultipleActiveResultSets=False;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    conn = pyodbc.connect(conn_str)
    return conn

def get_db_connection():
    conn_str = os.environ.get('SQLAZURECONNSTR_DB_CONNECTION_STRING')
    conn = pyodbc.connect(conn_str)
    return conn


@app.route('/')
def index():
    tasks_html = "<h2>Witaj! Aplikacja wdrożona przez GitHub Actions!</h2><ul>"
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Title FROM Tasks")
        rows = cursor.fetchall()
        for row in rows:
            tasks_html += f"<li>{row.Title}</li>"
        conn.close()
    except Exception as e:
        tasks_html += f"<li>Blad polaczenia z baza: {str(e)}</li>"

    tasks_html += "</ul>"
    return tasks_html
