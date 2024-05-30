import streamlit as st
import mysql.connector
import hashlib
import login, register

def create_connection():
    conn = mysql.connector.connect(
        host="sql.freedb.tech",
        user="freedb_anajesset",
        password="D9@WjYGE9?6&b&n",
        database="freedb_scpk_database"
    )
    return conn

def register_user(conn, username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    conn.commit()
    cursor.close()

def verify_login(conn, username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
    user = cursor.fetchone()
    cursor.close()
    return user

def is_registered():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return count > 1

def user():
    if not is_registered():
        register.register()
    else:
        login.register()

if __name__ == '__main__':
    user()
