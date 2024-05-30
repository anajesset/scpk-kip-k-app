import streamlit as st
from user import create_connection, register_user


def register():
    st.title('Registrasi Pengguna')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    confirm_password = st.text_input('Confirm Password', type='password')

    if password != confirm_password:
        st.error('Password dan konfirmasi password tidak cocok!')
        return

    if st.button('Register'):
        conn = create_connection()
        register_user(conn, username, password)
        st.success('Registrasi berhasil! Silakan login.')
        st.info('Silakan login menggunakan akun yang telah Anda daftarkan.')

if __name__ == "__main__":
    register()