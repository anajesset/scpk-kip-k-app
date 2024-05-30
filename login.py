import streamlit as st
from user import create_connection, verify_login, login

def login():
    st.title('Login Admin')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login', key=32134):
        conn = create_connection()
        user = verify_login(conn, username, password)
        if user:
            st.success(f'Login berhasil, Selamat datang, {username}!')
            return True
        else:
            st.error('Username atau password salah. Silakan coba lagi.')

if __name__ == "__main__":
    login()