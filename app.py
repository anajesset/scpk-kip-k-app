import streamlit as st
from user import is_registered, register, login
import home, daftar, ranking, prediksi, konsultasi

def main():
    st.title('SPK Penerima Bantuan KIP-K')

    if not is_registered():
        register()
        return
    
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        login_successful = login()
        if login_successful:
            st.session_state.logged_in = True
        else:
            st.warning('Silakan login terlebih dahulu!')
            return

    st.sidebar.title('Menu')
    menu_selection = st.sidebar.radio('Pilih Menu:', ('Home', 'Daftar', 'Ranking', 'Prediksi', 'Konsultasi'))

    if menu_selection == 'Home':
        st.switch_page('home.py')
    elif menu_selection == 'Daftar':
        st.switch_page('daftar.py')
    elif menu_selection == 'Ranking':
        st.switch_page('rangking.py')
    elif menu_selection == 'Prediksi':
        st.switch_page('prediksi.py')
    elif menu_selection == 'Konsultasi':
        st.switch_page('konsultasi.py')

if __name__ == "__main__":
    main()
