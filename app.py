import streamlit as st
from user import is_registered, register, login
import home, daftar, ranking, prediksi, konsultasi

def main():
    st.title('SPK Penerima Bantuan KIP-K')

    if 'register' not in st.session_state:
        st.session_state.register = False

    if not st.session_state.register:
        register_successfull = register()
        if register:
            st.session_state.register = True
        else:
            st.warning('Silakan login terlebih dahulu!')
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
        home.home()
    elif menu_selection == 'Daftar':
        daftar.daftar()
    elif menu_selection == 'Ranking':
        ranking.show_ranking()
    elif menu_selection == 'Prediksi':
        prediksi.prediksi()
    elif menu_selection == 'Konsultasi':
        konsultasi.chatbot()

if __name__ == "__main__":
    main()
