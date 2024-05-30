import streamlit as st
import google.generativeai as genai
from gtts import gTTS
from io import BytesIO

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang)
    output = BytesIO()
    tts.write_to_fp(output)
    output.seek(0)
    return output

def chatbot():
    api_key = 'AIzaSyA5s2_9M7Ngcc3Cr6Oo0s3yabB21MgUg0E'
    genai.configure(api_key=api_key)
    
    st.title('Konsultasi Bantuan KIP-K')
    
    language = st.radio("Pilih Bahasa:", ('Indonesia', 'English'))
    lang_code = 'id' if language == 'Indonesia' else 'en'
    
    generation_config = {
        "max_output_tokens": 1000,
        "temperature": 0.8,
        "top_p": 1
    }
    
    model = genai.GenerativeModel('gemini-pro')
    prompt = st.text_input("Masukan Pertanyaan Anda:")
    
    if st.button('Tanya'):
        if not prompt:
            st.warning('Tolong masukan pertanyaan anda')
        else:
            with st.spinner('Sistem sedang memproses pertanyaan yang Anda minta...'):
                response = model.generate_content(
                    prompt,
                    generation_config=generation_config,
                    stream=False
                )
                response_text = response.text
                st.write(response_text)
                
                audio_data = text_to_speech(response_text, lang_code)
                st.audio(audio_data, format='audio/mp3')

if __name__ == "__main__":
    chatbot()
