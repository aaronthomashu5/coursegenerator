import streamlit as st

def show_ppt():
    st.title("PowerPoint Outline")
    
    if 'ppt_text_body' not in st.session_state:
        st.error("No PPT content found. Please go back to the result page and click 'Generate PPT'.")
        return
    
    st.write(st.session_state.ppt_text_body)